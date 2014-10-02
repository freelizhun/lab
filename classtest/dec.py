class decorateAppleClass(object):
    def __init__(self, f):
        self.f = f
    
    def __call__(self, *args, **kargs):
        print("apple before call")
        result = self.f(*args, **kargs)
        print("apple after call")
        return result


@decorateAppleClass
def print_hello4():
    print("hello 4th time.")

print_hello4()
