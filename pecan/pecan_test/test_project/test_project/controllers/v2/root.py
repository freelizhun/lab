from test_project.controllers.v2 import meters
from test_project.controllers.v2 import query
from test_project.controllers.v2 import query2




class V2Controller(object):
    """Version 2 API controller root."""

    meters = meters.MetersController()
    query = query.QueryController()
    query2 = query2.QueryController2()
