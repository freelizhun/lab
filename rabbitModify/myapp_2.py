from webob import Request, Response
from pprint import pprint
import fileiter
import uuid
import hashlib
import os
from Connector.connector import Connector
from FileOp import FileOp

class Application(object):

    def __init__(self, conf):
        self.conn = Connector()
        pass

    def __call__(self, env, start_response):
       print '-------- into myapp ------'
       # fake data -----
       user_info=['test']
       filepath='/tmp/haha'
       #----------------
       req = Request(env)
       fileop = FileOp(user_info, filepath, req)
       if req.method=='PUT':
           ret = fileop.uploadData()
           return ret(env, start_response)
       if req.method=='GET':
           ret = fileop.downloadData()
           return ret(env, start_response)

   #return fileop
       #return self.handle_request(req)(env, start_response)

 
def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Application(conf)

