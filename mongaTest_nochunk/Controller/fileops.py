from webob.exc import HTTPAccepted, HTTPBadRequest, HTTPCreated, \
     HTTPInternalServerError, HTTPNoContent, HTTPNotFound, \
     HTTPNotModified, HTTPPreconditionFailed, HTTPOk, \
     HTTPRequestTimeout, HTTPUnprocessableEntity, HTTPMethodNotAllowed, \
     HTTPServiceUnavailable, HTTPUnauthorized

from fileop.FileOp import FileOp
import json

#from Controller.base import Controller

class FileOpsController(object):
    def __init__(self, app ):
        #Controller.__init__(self, app)
        
        print '------FileOps Init--------'
        pass

    def POST(self, req):
        print '-----into Fileops POST--------'
        user_info = ['test']
        filepath='/tmp/haha/a.txt'
        fop = FileOp(user_info, filepath, req)
        ret = fop.create_folder()
        print 'into get ----------------'
        
        #return HTTPOk(body ='TestController Running',content_type='application/json')
        print ret
        return ret

