import hashlib

m = hashlib.md5()
#594f803b380a41396ed63dca39503542
s = 'aaaaa'
m.update(s)
print m.hexdigest()

ss='aaa'
ss1= 'aa'
mmtest = hashlib.md5()
mmtest.update(ss)
print mmtest.hexdigest()

mm = hashlib.md5()
mm.update(ss1)
print mm.hexdigest()
