from webob import Request, Response
from pprint import pprint
    
class Application(object):

    def __init__(self, conf):
        self.testargv = conf.get('testargv','testla')
        pass

    def __call__(self, env, start_response):
       #self.app=app
       req = Request(env)
       #return self.app(env, start_response)
       print self.testargv
       return self.handle_request(req)(env, start_response)

    def handle_request(self, req):
        if (req.method == 'GET'):
            resp = Response(request=req)
            resp.body = 'you send GET method'
	    pprint(req.environ)
	    print req.body
            return resp
            #return self.app(env, req)
            
 
def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Application( conf)

