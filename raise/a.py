class MyError( Exception): 
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
def test():
    raise MyError(2*2)
def test2():
    print 'in test2'

try:
    test()
    test2()
except MyError, e:
    print 'my error:', e.value
