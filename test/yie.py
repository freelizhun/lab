

def a(aa,rev):
    count = 0
    for i in aa:
        yield i, count
        count = count+1
        print rev

rev=['rrr','eee','vvv']
aa =['aaaa','bbbb','ccccc']
count =0
for sa,count in a(aa, rev[count]):
    print sa, count
    
