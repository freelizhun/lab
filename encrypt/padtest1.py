

b=32
s=65
re = s%b

print re
print 'initial %d'%s
print b-re
after = b-re+s
print 'afterpad %d'%after

print b-(s%b)+s
if 0==re:
    padnum=0
else:
    padnum=b-(s%b)
print 'pading number'
print padnum

