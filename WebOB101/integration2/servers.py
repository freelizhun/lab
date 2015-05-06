from eventlet import wsgi, listen
#import myapp.MyApplication as
#from myapp import MyApplication
#import myapp.MyApplication as MyApplication
import myapp
#import wsgi
class Controller(object):
    def test22(self, mykey):
        print 'into the servers controller'
        #print("step 4: MyController's getlist(self, mykey) is invoked")
        return "get new controller"

def create_resource():
    return myapp.MyApplication(Controller())
    #return wsgi.Resource(Controller())
