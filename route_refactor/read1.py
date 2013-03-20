import eventlet
from eventlet import wsgi
from paste.deploy import loadapp
import os
from webob import Request, Response
from webob import exc
from pprint import pprint
import time

def hello_world(environ, start_response):
    #CHUNKSIZE = 65563
    CHUNKSIZE = 10
    request = Request(environ)
    #fname = request.args["file"]
    #print request.args["file"]
    fname='./savefile.txt'
    print fname
    #time.sleep(5)
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    print 'request size'
    print request_body_size
    print '--------------------'
    f = open(fname, "wb")
    print environ
    #chunk = environ["wsgi.input"].read(CHUNKSIZE)
    chunk = environ["wsgi.input"].read()
#    print chunk
#    while chunk:
#          f.write(chunk)
#          chunk = environ["wsgi.input"].read(CHUNKSIZE)
#          print chunk
#          print '--------------------'
    f.close()
    response = Response("success", mimetype='plain/text')
    return response(environ, start_response)
                                                         
if __name__ == "__main__":
    wsgi.server(eventlet.listen(('127.0.0.1', 8090)), hello_world)
