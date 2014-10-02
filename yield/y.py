import time
a = 0
def cal():
    global a
    a = a+1
    return a
def lo():
    s = cal()
    print 'lo',s
    yield s
lop = True
while lop:
    for h in lo():
        print h
        if h == 100:
            lop = False
"""
lop =True 
while lop:
    s = lo()
    if s == 100:
        lop = False
        #print s
    #else:
        #print s
"""
