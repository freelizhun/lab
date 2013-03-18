import hashlib

s = '12345678'*32*4*1000
print len(s)
print hashlib.sha1(s).hexdigest()
#----- method 2 -------------
m= hashlib.sha1()
m.update(s)
print m.hexdigest()
