import hashlib

s = '12345678'*32*4*1000
print len(s)
print hashlib.sha1(s).hexdigest()
