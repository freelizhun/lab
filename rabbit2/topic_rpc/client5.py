#!/usr/bin/env python
import pika
import sys
import uuid
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')
#result = channel.queue_declare(exclusive=True)
result = channel.queue_declare(queue='service1')
callback_queue = result.method.queue
global response
response = None
def on_response(ch, method, props, body):
    global response
    if corr_id == props.correlation_id:
        response = body
        print 'show response'
        print response
    #return response


routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
corr_id = str(uuid.uuid4())
channel.basic_consume(on_response, no_ack=True,
                           #queue=callback_queue)
                           queue='service2')
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      properties=pika.BasicProperties(
                                       reply_to = callback_queue,
                                       #reply_to = 'service1',
                                       correlation_id = corr_id,
                                       ),
                      body=message)
while response is None:
      print 'wait for response.....'
      connection.process_data_events()
      time.sleep(1)
print " [x] Sent %r:%r" % (routing_key, message)
connection.close()
