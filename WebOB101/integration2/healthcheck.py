from webob import Request, Response
from pprint import pprint
    
class ApplicationH(object):

    def __init__(self, app, conf):
        self.app=app
        self.conf = conf
        pass

    def __call__(self, env, start_response):
       req = Request(env)
       #return self.app(env, start_response)
       print 'into healthy'
       ret = self.handle_request(req)(env, start_response)
       return self.app(env, start_response)
       #return self.handle_request(req)(env, start_response)

    def handle_request(self, req):
        print 'print url %s'%req.url
        print 'print path_qs %s'%req.path_qs
        print 'print querystring %s'%req.query_string
        if (req.method == 'GET'):
            print '--------  file get ----------'
            resp = Response(request=req)
            print resp
            print 'into healthy'
            return resp
        if (req.method == 'PUT'):
            print '--------  file put ----------'
            resp = Response(request=req)
            print resp
            return resp
        
            
 
def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def healthcheck_filter(app):
          return ApplicationH(app, conf)
    return healthcheck_filter
    #return ApplicationH(app, conf)

