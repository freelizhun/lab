
global maxsize
global returnlen
global seg
maxsize =5
returnlen = 6
seg = 20

def getdata(a):
    r='a'
    count = 0
    maxdata = len(a)
    while count!=-1:
        init = count * 10
        fin = (count+1)* 10
        if fin>= maxdata:
            fin = maxdata 
        r = a[init: fin]
        yield r
        count = count + 1
        if fin == maxdata:
            break

def it(a):
    global maxsize
    global seg
    global returnlen
    print '--------'

    data = ''
    for i in getdata(a):
        counter = 0
        while (counter< len(i)):
            st =  int(i[counter:counter+maxsize])
            print st
            counter = counter + maxsize
            init = int(counter)
            fin = int(counter +st)
            print 'initial final',init, fin
            content = i[int(init): int(fin)]
            #content = i[5:6]
            print content
            counter = counter + len(content)
            print 'counter',counter
            data = data + content
            print counter, len(i)
        """
        if len(data) > returnlen:
            ret = data[0:returnlen]
            data = data[returnlen:]
            yield ret
        """
        
        
    """
    data = ''
    while len(data) < returnlen:
        i = getdata(a)
        print '---------------'
        print i
        segm = int(i[0:seg])
        data = data + i[segm:int(segm)]
        yield data
    """
        
def setupa():
    a = ''
    for i in range (1,seg+1):
        content = 'a'*i
        a= a + str(i).zfill(maxsize)+ content
    return a
a= setupa()
print a
for i in it(a):
    print i
#for i in it(a):



