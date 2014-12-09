

class Inout(object):
    def __init__(self, haha=None):
        if not haha:
            self.haha = 'haha' 
        else:
            self.haha = haha
    def __call__(self):
        print self.haha

print 'start run'

a = Inout('aaa')
a()
#or 
Inout()()
