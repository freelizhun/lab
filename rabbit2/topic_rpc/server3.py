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
#queue_name = result.method.queue

#binding_keys = sys.argv[1:]
binding_keys =["kern.*","*.critical"]
#if not binding_keys:
#    print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
#    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       #queue=queue_name,
                       queue='service1',
                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)
    response = 1000
    ch.basic_publish(exchange='',
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

channel.start_consuming()
