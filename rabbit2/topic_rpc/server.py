#!/usr/bin/env python
import pika
import sys
from updator import updatorServer 
import socket
    
def getqueueList():
    hostname = socket.gethostname()

    queue = ['all']
    return queue


binding_keys=[]
services = ['all','fop','mongodb']
functions=['update_software','sync_software','restart']


#example fop.mon0.function
def getBindingKey(hostname = None):
    if not hostname:
        hostname = socket.gethostname()
    else:
        hostname = 'mon'+hostname
    print 'hostname is:',hostname
    for service in services:
        for function in functions:
            print 
            binding_keys.append(service+'.'+function)
            binding_keys.append(service+'.'+hostname+'.'+function)
    print binding_keys
    return binding_keys    




update = updatorServer()

exchange_name = 'updator'
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.95.164'))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
                         type='topic')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print queue_name
binding_keys = getBindingKey(str(sys.argv[1]))
for binding_key in binding_keys:
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name,
                       #queue=queues,
                       routing_key=binding_key)


print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    def getfunction(key):
        return key.split('.')

    print 'in %s',sys.argv[1]
    print " [x] %r:%r" % (method.routing_key, body,)
    func = getfunction(method.routing_key)
    runstring = 'update.'+ func[-1]#method.routing_key
    service = func[0]
    print runstring
    ret = eval(runstring)(service)
    response = ret
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume(callback,
                      queue=queue_name)


channel.start_consuming()
