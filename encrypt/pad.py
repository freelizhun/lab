BLOCK_SIZE=32
PADDING = '{'
#s='12345'
s = u'1'*32

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
print pad
def pad(msg, block_size=BLOCK_SIZE, padding=PADDING):
    """
    *pad the text to be encrypted*
    - appends a padding character to the end of the String
    - until the string has block_size length

    """
    #return msg + ((block_size - len(msg) % block_size) * padding)
    print 'block size %d'%block_size
    print 'string size %d'%len(s)
    print 'padding size'
    print (block_size - (len(msg)%block_size))
    return msg + (block_size - (len(msg)%block_size))*padding
def depad(msg, padding=PADDING):
    """depad the decryptet message"""
    return msg.rstrip(padding)
print len(s)
encdata =  pad(s)
print len(encdata)
decdata = depad(encdata)
print len(decdata)


