import webob.dec
import eventlet
from eventlet import wsgi, listen
from routes import Mapper, middleware
 
 
class controller(object):
    def index(self):
        return "do index()"
 
    def add(self):
        return "do show()"
    def min(self):
        return "minimum"
 
class controller2(object):
    def servers(self):
        return "haha"
 
class App(object):
    def __init__(self):
        self.controller = controller()
        self.controller2 = controller2()
        m = Mapper()
        m.connect('blog', '/blog/{action}/{id}', controller=controller,
                  conditions={'method': ['GET']})
        m.connect('haha', '/haha/{action}/{id}', controller=controller2,
                  conditions={'method': ['GET']})
        self.router = middleware.RoutesMiddleware(self.dispatch, m)
 
    @webob.dec.wsgify
    def dispatch(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return 'error url: %s' % req.environ['PATH_INFO']
 
        action = match['action']
        if hasattr(self.controller2, action):
            func = getattr(self.controller2, action)
            ret = func()
            return ret
        else:
            return "has no action:%s" % action
 
    @webob.dec.wsgify
    def __call__(self, req):
        return self.router
 
if __name__ == '__main__':
    socket = listen(('0.0.0.0', 8000))
 
    server = eventlet.spawn(wsgi.server, socket, App())
    server.wait()
