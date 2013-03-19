


class Test(object):
    def __init__(self, stringla):
        self.stringla = stringla
        pass
    def __call__(self, stringla):
        print 'into Test'
        self.bprint(stringla)
        return 'haha'

    def bprint(self):
        print self.stringla
