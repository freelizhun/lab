import time

def _getModifyTime():
    return time.strftime("%a, %d %b %Y %H:%M:%S %z")
#Tue, 09 Apr 2013 03:29:20 +0000'
def _timeToValue(ha):
    print ha
    hha= ha.replace(':','').split()
    ss = str(hha[3]+hha[4])
    print ss
    return int(ss)

val=[]
val.append(_timeToValue(_getModifyTime()))
time.sleep(1)
val.append(_timeToValue(_getModifyTime()))
time.sleep(1)
val.append(_timeToValue(_getModifyTime()))
time.sleep(1)
valrandom=[]
valrandom.append(val[1])
valrandom.append(val[0])
valrandom.append(val[2])
print '---set random----'
print valrandom
print val
print '----sort-------'
valsort = sorted(valrandom, key=int)
print valsort






