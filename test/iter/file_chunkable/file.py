import fileiter

listfile=['aa.txt','bb.txt','cc.txt']
#x = iter(fileiter.FileIterable(listfile))
f = open('sum.txt','w')
for i in fileiter.FileIterable(listfile, 0, 4096000):
    #print i
    print len(i)
    f.write(i)

f.close()
