


def it(a):
    
    for i in range(a,100):
        if i % 10 ==0:
            yield i
        


a = 0
for i in it(a):
    print i
