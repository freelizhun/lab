import os
import time
#filelist = os.listdir(os.getcwd())
targetDir = '/opt/datetime'



def checkFileExpire():
    filelists = os.listdir(targetDir)
    print '------------------'
    print filelists
    filelist = []
    for ii in filelists:
        filelist.append(targetDir+'/'+ii)

    filelist = filter(lambda x: os.path.isdir(x), filelist)
    print filelist

    for fl in filelist:
        fll = fl
        print fll
        ff = os.listdir(fll)
        print 'ff',ff
        filel=[]
        for fff in ff:
            filel.append(fll+'/'+fff)
         
        print 'filelist', filel
        try:
            newest = max(filel, key=lambda x: os.stat(x).st_mtime)
            print 'the newest file',newest
            print 'show result'
            print os.stat(newest).st_mtime
            print time.time()
        except ValueError :
            print '-----empty file'
            #print os.stat(filel).st_mtime
            print '-----empty file'
        yield fl, True


for ss, tt in checkFileExpire():
    print 'show file', ss
    print 'show time',tt

#print newest


