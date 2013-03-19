from webob import Request, Response
from pprint import pprint
import fileiter
import uuid
import hashlib
import os
from Connector.connector import Connector

class Application(object):

    def __init__(self, conf):
        self.conn = Connector()
        pass

    def __call__(self, env, start_response):
       print '-------- into myapp ------'
       req = Request(env)
       return self.handle_request(req)(env, start_response)
    def createUUID(self):
        return uuid.uuid1()
    def getCheckSum(self, chunk):
        return hashlib.sha1(chunk).hexdigest()
    def uploadData(self, req, ud):
            print 'the uuid is %s'%ud
            ud='aaa'
            CHUNKSIZE = 1024000
            filename = req.environ.get('QUERY_STRING')
            fname=filename.split('=')[1]
            print fname
            #time.sleep(5)
            #f = open(fname, "w")
            #chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
            # ----------  write files ----------------
            print 'bbbb'
            #print chunk
            count=0
            chunk='init'
            while chunk:
                chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
                if len(chunk)==0:
                    break;
                print '--------------------'
                checksum = self.getCheckSum(chunk)

                print 'checksum %s'%checksum
                print 'length %d'%len(chunk)
                ret = self.conn.writeData(ud, chunk, checksum)
                #f.write(chunk)
                #print chunk
                count=count+1
                print count
            
            #f.close()
            resp = Response(request=req)
            resp.body = 'save over'
            pprint(req.environ)
            print req.body
            return resp
    def handle_request(self, req):

        if (req.method == 'GET'):
            #resp = Response(request=req)
            #data = open('./save.jpg', 'r').read()
            #data = open('./save.jpg', 'r')
            #resp = Response(app_iter = data, request=req)
            resp = Response(request=req)
            chunksize=1024000
            resp.app_iter = fileiter.FileIterable('./random.txt',chunksize)
            #resp.app_iter = fileiter.FileIterable('./random.txt')
            #resp.app_iter=data
            #resp = Response(request=req)
	    pprint(req.environ)
	    print req.body
            return resp
        if (req.method == 'POST'):
                ud = self.createUUID()
                return self.uploadData(req, ud)


 
def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Application(conf)

