import hashlib

SECRET_KEYST = u'a1b2c3d4e5f6g7h8a1b2c3d4e5f6g7h8'
message='python'
filename =  hashlib.sha1(message).hexdigest()
s= filename[0:32]
print s

print SECRET_KEYST
