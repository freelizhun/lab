from webob import Request, Response
from webob import exc
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
       #if req.method=='POST':
       #     status = '500 OK'
       #     response_headers = [('Content-type','application/json')]
       #     start_response(status, response_headers)
       #     return ['Hello world!n']
       retfunc='returnback'
       if retfunc == self.checkresult(req, env, start_response):
            status = '500 OK'
            response_headers = [('Content-type','application/json')]
            start_response(status, response_headers)
            return ['Hello World!n']
            
        #return resp
       #self.checkresult(req, env, start_response)
       #ret = self.handle_request(req)(env, start_response)
       ret = self.handle_request(req)
       return self.app(env, start_response)
       #return self.handle_request(req)(env, start_response)
    def checkresult(self, req, env, start_response):
        print '------ into check result -------'
        if req.method=='PUT':
            print ' ---- into POST drop -----'
            #status = '500 OK'
            #response_headers = [('Content-type','application/json')]
            #start_response(status, response_headers)
            return 'returnback'
    #def handle_request(self, req):
    def handle_request(self, req):
        #req = Request(env)
        print 'print url %s'%req.url
        print 'print path_qs %s'%req.path_qs
        print 'print querystring %s'%req.query_string
        if (req.method == 'GET'):
            print '--------  file get ----------'
            print req.environ
            print 'body-------------'
            print req.headers.get('Content-Type')
            print req.body
            resp = Response(request=req)
            print resp
            print req.GET.getall('q')
            print 'into healthy'
            return resp
        if (req.method == 'PUT'):
            print '--------  file put ----------'
            resp = Response(request=req)
            print resp

        #return resp
        
            
 
def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def healthcheck_filter(app):
          return ApplicationH(app, conf)
    return healthcheck_filter
    #return ApplicationH(app, conf)

