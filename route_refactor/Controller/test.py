from webob.exc import HTTPAccepted, HTTPBadRequest, HTTPCreated, \
     HTTPInternalServerError, HTTPNoContent, HTTPNotFound, \
     HTTPNotModified, HTTPPreconditionFailed, HTTPOk, \
     HTTPRequestTimeout, HTTPUnprocessableEntity, HTTPMethodNotAllowed, \
     HTTPServiceUnavailable, HTTPUnauthorized


#from Controller.base import Controller

class TestController(object):
    def __init__(self, app ):
        #Controller.__init__(self, app)
        print '------haha--------'
        pass
    def GET(self, req):
        print 'into get ----------------'
        return HTTPOk(body ='TestController Running',content_type='application/json')
