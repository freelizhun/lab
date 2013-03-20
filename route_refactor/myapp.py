from webob import Request, Response
from pprint import pprint
import fileiter
import uuid
import hashlib
import os
from Connector.connector import Connector
from FileOp import FileOp
from Controller.test import TestController
from routes import Mapper
from webob.exc import HTTPAccepted, HTTPBadRequest, HTTPForbidden, \
            HTTPMethodNotAllowed, HTTPNotFound, HTTPPreconditionFailed, \
                HTTPRequestEntityTooLarge, HTTPRequestTimeout, HTTPServerError, \
                    HTTPServiceUnavailable, status_map

class BaseApplication(object):
    special_vars = ['controller','action']
    def __init__(self, conf):
        self.mapper = Mapper()

        self.mapper.connect('/test',controller = TestController,
                                conditions = dict(method=['GET']))
        #self.mapper.connect('/test',controller = TestController)

    def __call__(self, env, start_response):
        req = Request(env)
        return self.handle_request(req)(env, start_response)

    def handle_request(self, req):
        print 'into mapping'
        results = self.mapper.routematch(environ=req.environ)
        print 'results --- after mapping'
        print '---- show result -----'
        print results
        match, route = results
        controller = match['controller'](self)
        try:
            handler = getattr(controller, req.method)
        except AttributeError:
            return HTTPMethodNotAllowed(request = req)
        #getattr(handler, 'publicly_accessible')
        kwargs = match.copy()
        for attr in self.special_vars:
            if attr in kwargs:
                 del kwargs[attr]
        #return handler(req, **kwargs)
        return handler(req, **kwargs)



class Application(BaseApplication):
    def handle_request(self, req):
        req.response = super(Application, self).handle_request(req)
        return req.response

   #return fileop
       #return self.handle_request(req)(env, start_response)

 
def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Application(conf)

