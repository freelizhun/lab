#import logging
from decorator import decorator
from monga.common import response as RESP
import sys

class BadRequestError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class NotFoundError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class ForbiddenError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InternalServerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotImplementError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class OverQuotaError(Exception):
    pass

class ManifestUploadError(Exception):
    pass

def handle_exceptions():
    def wrapper(func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as e:
            return RESP.bad_request(e)
        except NotFoundError as e:
            return RESP.not_found(e)
        except ForbiddenError as e:
            return RESP.forbidden(e)
        except NotImplementError:
            return RESP.not_found('Not Implement')
        except InternalServerError as e:
            return RESP.internal_error(e)
        except UnauthorizedError as e:
            return RESP.unauthorized('Unauthorized')
        #except Exception as e:
        #    return RESP.internal_error(e)
    return decorator(wrapper)
