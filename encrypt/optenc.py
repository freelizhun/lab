import hashlib
#from encutils import encData
import encutils as enc
import time


message='test'
print message
filename= hashlib.sha256(message).hexdigest()
print filename
print str(filename)


enc = enc.encData()

#our_data_to_encrypt = u'123456789'*32*4*1000*100
our_data_to_encrypt = u'0'*4030000
print 'original size %d Mbyte'%(int(len(our_data_to_encrypt))/1000000.)



print 'start encrypt'
start = time.time()
enc_data = enc.encrypt(our_data_to_encrypt, filename)
end = time.time()
print (end-start)
print 'size %d'%len(enc_data)

print 'into decription'
dec_data = enc.decrypt(enc_data, filename)
print 'size %d'%len(dec_data)


if dec_data == our_data_to_encrypt:
    print 'same data after decrypt'
else:
    print 'nononoono'
   

