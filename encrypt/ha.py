import hashlib
message = 'python'
print hashlib.sha1(message).hexdigest()
print len(hashlib.sha256(message).hexdigest())
