
from pecan import rest
import pecan




class MetersController(rest.RestController):
    """Works on meters."""

    #@pecan.expose()
    #def _lookup(self, meter_name, *remainder):
    #    return MeterController(meter_name), remainder

    #@wsme_pecan.wsexpose([Meter], [base.Query])
    @pecan.expose()
    #def get_all(self, q=None):
    def get(self):
        print 'hahah'
        return "haha"




