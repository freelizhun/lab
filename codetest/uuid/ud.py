
import uuid
print uuid.uuid1()
print uuid.uuid5(uuid.NAMESPACE_DNS,'ss')
print str(uuid.uuid5(uuid.NAMESPACE_DNS,'s'))
hashla = '0132ca642aee4550940ccba6a5d96b48/size1.txt'
print str(uuid.uuid5(uuid.NAMESPACE_DNS, hashla))
