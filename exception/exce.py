from decorator import decorator
import sys

class BadRequestError(Exception):
    def __init__(self):
        self.value = 'hahahahaha'
    def __str__(self):
        return repr(self.value)

def returnsignal(e):
    print e
    return e
def handle_exceptions():
    def wrapper(func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as e:
            return returnsignal(e)

        #except Exception as e:
        #    return RESP.internal_error(e)
    return decorator(wrapper)

