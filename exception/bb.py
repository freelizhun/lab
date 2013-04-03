
from exce import *

class teste(object):
    def __init__(self):
        pass
    def bprint(self):
        print 'in teste'
        raise BadRequestError()
