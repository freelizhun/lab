from webob import Request, Response
from pprint import pprint
import fileiter
import uuid
import hashlib
import os
from Connector.connector import Connector

class FileOp(object):

    def __init__(self, user_id, filepath, req ):
        print 'into FileOp-----------------'
        self.conn = Connector()
        self.user_id = user_id
        self.filepath = filepath
        self.req = req
        pass

    #def __call__(self):
    #   print '-------- into myapp ------'
       #req = Request(env)
    #   return self.handle_request(self.req)
    def createUUID(self):
        return uuid.uuid1()
    def getCheckSum(self, chunk):
        return hashlib.sha1(chunk).hexdigest()

    
    def _uploadData(self, req, ud):
            print 'the uuid is %s'%ud
            ud='aaa'
            CHUNKSIZE = 1024000
            #filename = req.environ.get('QUERY_STRING')
            #fname=filename.split('=')[1]
            fname = req.headers.get('Filepath')
            print fname
            #time.sleep(5)
            #f = open(fname, "w")
            #chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
            # ----------  write files ----------------
            print 'bbbb'
            #print chunk
            print req.environ
            count=0
            rawcount = 0
            chunk='init'
            datasize = int(req.environ.get('CONTENT_LENGTH'))
            #while rawcount < datasize:
            #while chunk or rawcount < datasize:
            network_chunk_size =  1024000
            reader = req.environ['wsgi.input'].read
            for chunk in iter(lambda: reader(network_chunk_size), ''):
                checksum = self.getCheckSum(chunk)
                rawcount = rawcount + len(chunk)
                print rawcount
                ret = self.conn.writeData(ud, fname, chunk, checksum)
            """
            while chunk :
                try:
                    print 'read chunk'
                    chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
                    print '--------------------'
                    checksum = self.getCheckSum(chunk)
                    rawcount = rawcount + len(chunk)
                    print rawcount

                    print 'checksum %s'%checksum
                    print 'length %d'%len(chunk)
                    ret = self.conn.writeData(ud, fname, chunk, checksum)
                    #f.write(chunk)
                    #print chunk
                    count=count+1
                    print count
                except:
                    print '---------connection break----------'
                    resp = Response(request=req)
                    resp.body = 'connection break'
                    return resp
            """
            print 'total size:',rawcount
                    
            ret = self.conn.commit()
            print 'commit over'
            #f.close()
            #resp = Response(request=req)
            resp = Response('200 OK')
            resp.body = 'save over'
            #pprint(req.environ)
            #print req.body
            return resp
    def _downloadData(self, req):
        if (req.method == 'GET'):
            #resp = Response(request=req)
            #data = open('./save.jpg', 'r').read()
            #data = open('./save.jpg', 'r')
            #resp = Response(app_iter = data, request=req)
            resp = Response(request=req)
            chunksize=1024000
            uid='aaa'
            fp = req.headers.get('Filepath')
            chunkList = self.conn.readMeta(fp)
            print ' --------- snow chunk list --------'
            print chunkList
            print 'into app_iter'
            resp.app_iter = fileiter.FileIterable(chunkList)
            print 'left app_iter'
            #resp.app_iter = fileiter.FileIterable('./random.txt')
            #resp.app_iter=data
            #resp = Response(request=req)
            #pprint(req.environ)
            #print req.body
            return resp
    def handle_request(self, req):

        if (req.method == 'GET'):
            #resp = Response(request=req)
            #data = open('./save.jpg', 'r').read()
            #data = open('./save.jpg', 'r')
            #resp = Response(app_iter = data, request=req)
            resp = Response(request=req)
            chunksize=1024000
            uid='aaa'
            chunkList = self.conn.readMeta(uid)
            print ' --------- snow chunk list --------'
            print chunkList
            resp.app_iter = fileiter.FileIterable(chunkList)
            #resp.app_iter = fileiter.FileIterable('./random.txt')
            #resp.app_iter=data
            #resp = Response(request=req)
            #pprint(req.environ)
            #print req.body
            return resp
        #if (req.method == 'POST'):
        #        ud = self.createUUID()
        #        return self.uploadData(req, ud)
    def uploadData(self):
        ud = self.createUUID()
        ret =  self._uploadData(self.req, ud)
                    
        print '--------into upload-------------'
        #print ret
        return ret
    def downloadData(self):
        ret =  self._downloadData(self.req)
        print '--------into download-------------'
        #print ret
        return ret



 
#def app_factory(global_conf, **local_conf):
#    conf = global_conf.copy()
#    conf.update(local_conf)
#    return Application(conf)

