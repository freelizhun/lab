import md5
import uuid

s1 = '%01DC3%23DCD'
su = u'%01DC3%23DCD'
print ' using md5 ---------'
print md5.new(s1).hexdigest()
print md5.new(su).hexdigest()
print 'translate unicode to ascii'
import unicodedata
sustr =  unicodedata.normalize('NFKD', su).encode('ascii','ignore')
print uuid.uuid5(uuid.NAMESPACE_DNS, sustr)

print ' using uuid; not suport for unicode--------'
print uuid.uuid5(uuid.NAMESPACE_DNS, s1)
print uuid.uuid5(uuid.NAMESPACE_DNS, su)



