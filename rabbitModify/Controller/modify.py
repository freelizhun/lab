from webob.exc import HTTPAccepted, HTTPBadRequest, HTTPCreated, \
     HTTPInternalServerError, HTTPNoContent, HTTPNotFound, \
     HTTPNotModified, HTTPPreconditionFailed, HTTPOk, \
     HTTPRequestTimeout, HTTPUnprocessableEntity, HTTPMethodNotAllowed, \
     HTTPServiceUnavailable, HTTPUnauthorized

import pika
import sys
import time
import eventlet

#from Controller.base import Controller
def waitformq(severities):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs',
                             type='direct')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    #severities = sys.argv[1:]
    if not severities:
        print >> sys.stderr, "Usage: %s [info] [warning] [error]" % \
                             (sys.argv[0],)
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(exchange='direct_logs',
                           queue=queue_name,
                           routing_key=severity)

    print ' [*] Waiting for logs. To exit press CTRL+C'
    
    def callback(ch, method, properties, body):
        print " [x] %r:%r" % (method.routing_key, body,)
        raise disc
    try:
        channel.basic_consume(callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()
    except:
        channel.stop_consuming()
        print 'exception to stop'
    return None

    

class ModifyController(object):
    def __init__(self, app ):
        #Controller.__init__(self, app)
        
        print '------haha--------'
        pass


    def GET(self, req):
        #test=['test','haha']
        test=[]
        #while True:
        #    eventlet.sleep(1)
        #time.sleep(100)
        #waitformq(test)
        #pool=eventlet.GreenPool() 
        #pool.spawn(waitformq, test)
        #pool.waiting()
        test.append(req.environ.get('HTTP_X_META_NOTIFY'))
        waitformq(test)
        return HTTPOk(body ='download over----',content_type='application/json')
        """
        print '-----into get--------'
        print req
        resp = Response("200 OK")
        resp.headers['Content-Type']='application/json'
        #print '--------into upload-------------'
        print 'return resp upload'
        return resp
        """

