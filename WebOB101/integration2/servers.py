from eventlet import wsgi, listen
import myapp
class Controller(object):
    def test22(self, mykey):
        print 'into the servers controller'
        return "get new controller"
    def test11(self, mykey):
        print 'into the servers controller'
        return "get test11"
    def __haha(self, mykey):
        print 'into the servers controller'
        return "get haha"

def create_resource():
    return myapp.Resource(Controller())
