
from pecan import rest, request
import pecan
#from wsmeext.pecan import wsexpose
from wsmeext.pecan import wsexpose


class QueryController(rest.RestController):

    # we need to define the test function
    _custom_actions = {
        'testla': ['GET'],
        'input': ['GET'],
    }
    #@pecan.expose()
    #def _lookup(self, meter_name, *remainder):
    #    return MeterController(meter_name), remainder

    #@wsme_pecan.wsexpose([Meter], [base.Query])
    """
    def __init__(self, user_id='test'):
        self.user_id = user_id

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return QueryController(user_id), remainder

    """

    @pecan.expose()
    def get(self):
        print 'return query'
        #print self.user_id
        return "query get"
    @pecan.expose()
    def post(self):
        return "query post"

    @pecan.expose()
    def testla(self):
        return "fadsfasdf"

    # where the input is:  curl 'localhost:8080/v2/query/input?number=3&check=aaa'  need '' alot
    # the first int is output, but it dosen't check too much
    @wsexpose(unicode, int, unicode)    
    def input(self, number, check):
        print number
        print self.user_id
        return 'aaa'




