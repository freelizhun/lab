#!/usr/bin/env python
import pika
import sys
from updator import updatorServer 
import socket
    
def getqueueList():
    hostname = socket.gethostname()

    queue = ['all']
    return queue
update = updatorServer()

exchange_name = 'updator'
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
                         type='direct')

#result = channel.queue_declare(exclusive=True)
#queueList = getqueueList()
queues = 'all'
result = channel.queue_declare(queue=queues)
result1 = channel.queue_declare(queue='not')
#queue_name = result.method.queue

#binding_keys = sys.argv[1:]
#binding_keys =["kern.*","*.critical"]
binding_keys=['update_software','sync_software']

for binding_key in binding_keys:
    channel.queue_bind(exchange=exchange_name,
                       #queue=queue_name,
                       queue=queues,
                       routing_key=binding_key)

for binding_key in binding_keys:
    channel.queue_bind(exchange=exchange_name,
                       #queue=queue_name,
                       queue='not',
                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)
    runstring = 'update.'+method.routing_key
    ret = eval(runstring)()
    #if method.routing_key == 'update_software':
    #    updateSoftware()
    #response = 1000
    print 'start to return'
    response = ret
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


#channel.basic_consume(callback,
#                      queue=queue_name,
#                      no_ack=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queues)
channel.basic_consume(callback,
                      queue='not')


channel.start_consuming()
