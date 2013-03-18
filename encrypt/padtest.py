

b=32
s=64
re = s%b

print re
print 'initial %d'%s
print b-re
after = b-re+s
print 'afterpad %d'%after

print b-(s%b)+s
padnum=b-(s%b)
print padnum

