class BadRequestError(Exception):
    def __init__(self):
        print 'Error'
        self.value='Error'
        pass
    def __str__(self):
        return self.value
s=True
try:
    if s:
        raise BadRequestError()
except BadRequestError as e:
    print 'haha'
    print e
