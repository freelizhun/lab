
from pecan import rest, request
import pecan
#from wsmeext.pecan import wsexpose
from wsmeext.pecan import wsexpose

#curl localhost:8080/v2/query2/namehaha/name
#where namehaha is parameter and name is routeing attribute
#curl localhost:8080/v2/query2/namehaha will routing to get function, they can co-exist in same class
import commands
class NextController(rest.RestController):
    _custom_actions = {
        'name': ['GET'],
    }
    def __init__(self, user_id=None):
        print 'into next init'
        print 'the userid is %s'%user_id
        self.user_id = user_id

    @pecan.expose()
    def get(self):
        return 'next controller get routing'

    @pecan.expose()
    def name(self):
        strcmd='dd if=/dev/urandom of=/root/%s bs=1G count=10'%self.user_id
        commands.getstatusoutput(strcmd)
        return 'next controller name routing'

class QueryController2(rest.RestController):
    #@pecan.expose()
    #def _lookup(self, meter_name, *remainder):
    #    return MeterController(meter_name), remainder

    #@wsme_pecan.wsexpose([Meter], [base.Query])
    #def __init__(self, user_id=None, user_id1=None):
    #    self.user_id = user_id
    #    self.user_id1 = user_id1
    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        if user_id:
            print ' into next controller'
            return NextController(user_id), remainder


    @pecan.expose()
    def get(self):
        print 'return query'
        return "query2 get"
    @pecan.expose()
    def post(self):
        return "query post"




