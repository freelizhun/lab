import webob.dec
import webob
import eventlet
from eventlet import wsgi, listen
from routes import Mapper, middleware
 
 


class MyController(object):
    def getlist(self, mykey):
        print("step 4: MyController's getlist(self, mykey) is invoked")
	return "get key la"

class MyController2(object):
    def gettable(self, mykey):
        print("step 4: MyController's getlist(self, mykey) is invoked")
	return "get table la"
    def getchair(self, mykey):
	return "get chair la"
    def getbeer(self, mykey):
	self.__test(mykey)
	return "get beer"
    #__ will not as a router
    def __test(self,mykey):
	print 'goto __test'
	return "get __test"


class MyApplication(object):
    """Test application to call from router."""

    def __init__(self, controller):
        self._controller = controller
        
    def __call__(self, environ, start_response):
        print("step 3: MyApplication is invoked")
        
        action_args = environ['wsgiorg.routing_args'][1].copy()
        try:
            del action_args['controller']
        except KeyError:
            pass

        try:
            del action_args['format']
        except KeyError:
            pass
        
        action = action_args.pop('action', None)
        controller_method = getattr(self._controller, action)
        result = controller_method(**action_args)
        
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [result]


class Router(object):  
    """WSGI middleware that maps incoming requests to WSGI apps."""  
  
    def __init__(self):  
        # if we're only running in debug, bump routes' internal logging up a  
        # notch, as it's very spammy  
 	my_application = MyApplication(MyController()) 
        self.mapper = Mapper() 
        route_name = "dummy_route"
        route_path = "/dummies"
	self.mapper.connect(route_name, route_path,
                        controller=my_application,
                        action="getlist",
                        mykey="myvalue",
                        conditions={"method": ['GET']})

 	my_application2 = MyApplication(MyController2()) 
	self.mapper.connect("test","/test/{action}",
			controller=my_application2,
			mykey="myvalue",
                        conditions={"method": ['GET']})

        self.map = self.mapper  
        self._router = middleware.RoutesMiddleware(self._dispatch,  
                                                          self.map)  
 
    @webob.dec.wsgify(RequestClass=webob.Request)  
    def __call__(self, req):  
        """Route the incoming request to a controller based on self.map. 
 
        If no match, return a 404. 
 
        """  
        return self._router  
 
    @staticmethod  
    @webob.dec.wsgify(RequestClass=webob.Request)  
    def _dispatch(req):  
        """Dispatch the request to the appropriate controller. 
 
        Called by self._router after matching the incoming request to a route 
        and putting the information into req.environ.  Either returns 404 
        or the routed WSGI app's response. 
 
        """  
        match = req.environ['wsgiorg.routing_args'][1]  
	if not match:
            return webob.exc.HTTPNotFound()
	print '###############'
	print match
	print '###############'
        app = match['controller']  
        return app   
 
if __name__ == '__main__':
    socket = listen(('0.0.0.0', 8000))
 
    #server = eventlet.spawn(wsgi.server, socket, App())
    server = eventlet.spawn(wsgi.server, socket, Router())
    server.wait()
