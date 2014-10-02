# coding=UTF-8
filename ='chi.txt'
 
f = open(filename, 'r')
b_str = f.read()
f.close()
print b_str 
print b_str.decode('utf-8') # 這是什麼？
print '哈'.encode('utf-8')
print b_str.decode('utf-8').encode('utf-8') # 這是什麼？
if b_str=='哈'.encode('UTF-8'):
    print "yes"
