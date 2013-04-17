

def combine(*ss):
    print ss
    for i in ss:
        for ii in i:
            print ii

a = ['aaa']
b = ['bbb']
combine(a, b)
