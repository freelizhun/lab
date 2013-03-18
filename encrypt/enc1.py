from Crypto.Cipher import AES
key =u'0123456789abcdef'
IV = u'12345678abcdefgh'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV)
#text = 'j'*64+'i'*128
#text = u'123456789012345678901234567890abc'*10
#text = u'12345678'*40960
text = u'12345678'*32*1000


print 'size %d'%len(text)
#print text
ciphertext = encryptor.encrypt(text)
#print ciphertext
print 'enc size %d'%len(ciphertext)

decryptor= AES.new(key,mode, IV)
plain = decryptor.decrypt(ciphertext)
print 'dec size %d'%len(plain)
#print plain
