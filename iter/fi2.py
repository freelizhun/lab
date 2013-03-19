import time
global headersize
global returnlen
global seg
global a
headersize =5
returnlen = 20
seg = 100
a = ''


global chunkRawData
chunkRawData = ''
global rawdata
rawdata = ''
# remove it a;
#all data got by getheader or getdfata.
global rawcount 
rawcount=0
def getrawdata():
    global rawcount 
    print '-----------', rawcount, len(a)
    if rawcount >= len(a):
        print 'return empty'
        return ''
    init = rawcount 
    fin = init + 20
    if fin > len(a):
        fin = len(a)
    rawcount = rawcount + (fin-init)
    print '---- range ------', init, fin
    return a[init:fin]

def getheader(counter):
    global chunkRawData
    global a
    global rawdata
    print 'getheader ---------'
    #rawdata = a
    if len(rawdata)  <= (counter + headersize): 
        print 'header get rawdata'
        tmpdata = getrawdata()
        if tmpdata=='':
            return 0, None
        rawdata = rawdata + tmpdata
    init = counter
    fin = counter + headersize
    return fin, int(rawdata[init:fin])

def getdata(counter, size):
    global chunkRawData
    global a
    global rawdata

    print 'getdata ---------'
    while(len(rawdata)<=(counter + size)):
        print 'data get rawdata'
        tmpdata = getrawdata()
        print 'tmpdata is',tmpdata
        rawdata = rawdata + tmpdata
        if tmpdata == '':
            break
    #rawdata = a
    init = counter
    fin = counter + size
    return fin, rawdata[init:fin]
    

def it():
    global headersize
    global seg
    global returnlen
    global a
    chunkdata = ''
    data = ''
    counter = 0
    while(True):
        (counter, header) = getheader(counter)
        print 'header',header
        if header is not None:
            print counter, header
            (counter, data) = getdata(counter, header)
            chunkdata = chunkdata + data
            print 'show counter and data'
            print counter, data
            #sendcounter = 0
            if data != '':
                while len(chunkdata) >= returnlen:
                    print 'length compare',len(chunkdata), returnlen
                    #sendcounter = sendcounter + returnlen
                    yield chunkdata[0:returnlen]
                    chunkdata = chunkdata[returnlen:]
                yield chunkdata[0:len(chunkdata)]
                chunkdata = ''
            else:
                #yield chunkdata[0:len(chunkdata)]
                yield chunkdata[0:returnlen]
        else:
            print 'data finished'
            break
    #yield None
        
def setupa():
    global a
    a = ''
    for i in range (1,seg+1):
        content = 'a'*i
        a= a + str(i).zfill(headersize)+ content
    return a
a= setupa()
print a
#time.sleep(3)
#return fixsize
suma = 0
for i in range(1,seg+1):
    suma = suma + i
sumres= 0
sumcount = 1
for i in it():
    print 'return data'
    print 'i len',len(i)
    sumres = sumres + len(i)
    print 'final comprare',len(i), sumcount
    sumcount = sumcount + 1 


print sumres, suma
if sumres != suma:
    print 'something wrong'
#for i in it(a):



