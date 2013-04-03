from exce import *
from bb import teste
def testinsystem():
    #raise BadRequestError()
    te = teste()
    te.bprint()
    

@handle_exceptions()
def ss():
    testinsystem()
    
    #raise BadRequestError()
ss()
