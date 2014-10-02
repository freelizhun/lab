def filter(a):
    a.pop('aaa')
    a.pop('ccc')
    return a


a ={'aaa':'bbb','ccc':'ddd', 'eee':'fff'}
b = filter(a)
print b
