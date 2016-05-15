from test_project.controllers.v2 import meters




class V2Controller(object):
    """Version 2 API controller root."""

    meters = meters.MetersController()
