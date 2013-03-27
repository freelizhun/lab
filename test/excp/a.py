


import excep as exception
from exception import *



@exception.handle_exceptions()
def test():
    #raise ZeroDivisionError()
    a = 10.
    b=0
    #a/b
    if b==0:
        raise BadRequestError('Access denied')

test()
