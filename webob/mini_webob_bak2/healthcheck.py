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
       return self.app(env, start_response)
       #return self.handle_request(req)(env, start_response)

    def handle_request(self, req):
        if (req.method == 'GET'):
            resp = Response(request=req)
            print 'into healthy'
            return resp
            
 
def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def healthcheck_filter(app):
          return ApplicationH(app, conf)
    return healthcheck_filter
    #return ApplicationH(app, conf)

