
class testError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class notError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def test(ii):
    if ii == 1:
        raise testError('connectino')
    if ii==2:
        raise notError('cccc')
    if ii==3:
        raise hhotError('hahaha')

try:
    test(2)
    print 'test over'
except testError as e:
    print e
except notError as e:
    print e
except:
    print 'except'
