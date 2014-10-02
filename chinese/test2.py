# -*- coding: utf-8 –*- 
print type('hahah')
print type('哈哈')
print type(u'哈哈')
print type(unicode('中文','utf-8'))
s1 = u'哈哈'
#s2 = unicode('中文','utf-8')
s2 = unicode('哈哈','utf-8')
print s1
print s2

filename ='chi.txt'

f = open(filename, 'r')
b_str = f.read()
b_str=b_str.strip()
f.close()

print type(b_str)
s3 = unicode(b_str,'utf-8')
print s3, type(s3)
print s1,s2,s3
print len(s1),len(s2),len(s3)

if s1 == s2:
    print 'yes'
else:
    print 'no'
if s2 == s3:
    print 'yes'
else:
    print 'no'

if s1 == s3:
    print 'yes'
else:
    print 'no'
