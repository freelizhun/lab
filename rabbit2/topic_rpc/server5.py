#!/usr/bin/env python
import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

#result = channel.queue_declare(exclusive=True)
result = channel.queue_declare(queue='service1')
result = channel.queue_declare(queue='service2')
#queue_name = result.method.queue

#binding_keys = sys.argv[1:]
binding_keys =["kern.*","*.critical"]
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       #queue=queue_name,
                       queue='service1',
                       routing_key=binding_key)

binding_keys1 =["warn.*","*.notcritical"]
for binding_key1 in binding_keys1:
    channel.queue_bind(exchange='topic_logs',
                       queue='service2',
                       routing_key=binding_key1)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)
    response = 1000
    ch.basic_publish(exchange='topic_logs',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

def callback2(ch, method, properties, body):
    print "in 2 [x] %r:%r" % (method.routing_key, body,)
    response = 2000
    ch.basic_publish(exchange='topic_logs',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

#channel.basic_consume(callback,
#                      queue=queue_name,
#                      no_ack=True)
channel.basic_consume(callback,
                      queue='service1')

channel.basic_consume(callback2,
                      queue='service2')

channel.start_consuming()
