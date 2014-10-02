#!/usr/bin/env python
import pika
import json
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
#connection = pika.SelectConnection(pika.ConnectionParameters(
#        host='localhost'))
print 'goto next'
channel = connection.channel()

channel.queue_declare(queue='rpc_queue1')
channel.queue_declare(queue='rpc_queue2')


#connection1 = pika.BlockingConnection(pika.ConnectionParameters(
#        host='localhost'))
#channel1 = connection1.channel()

#channel.exchange_declare(exchange='direct_logs',
#                         type='direct')

#result = channel.queue_declare(exclusive=True)
#queue_name = result.method.queue

#severities = sys.argv[1:]
#if not severities:
#    print >> sys.stderr, "Usage: %s [info] [warning] [error]" % \
#                         (sys.argv[0],)
#    sys.exit(1)
#for severity in severities:
#    channel.queue_bind(exchange='direct_logs',
#                       queue=queue_name,
#                       routing_key=severity)
def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    #n = int(body)
    dic = json.loads(body)
    print dic
    n = int(dic.get('aaa'))
    n1 = int(dic.get('bbb'))
    print 'here is n1',n1
    #n1 = dict(body)
    #n = n1.get('aaa')
    #n1 = int(body1)
    print " [.] fib(%s)"  % (n,)
    response = fib(n)
    print props.reply_to
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue1')
channel.basic_consume(on_request, queue='rpc_queue2')

print " [x] Awaiting RPC requests"
#channel.start_consuming()

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
print " [x] start log server"
