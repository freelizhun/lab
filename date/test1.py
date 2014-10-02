import os
import time
#filelist = os.listdir(os.getcwd())
targetDir = '/opt/monga/temp'

expireTime = 100
runDelay = 5


def getsubdir(target, retmain=False):
    filelistss = os.listdir(target)
    retfile=[]
    for filelists in filelistss:
        retfile.append(target+'/'+filelists)
    if retmain:
        retfile.append(target)
    return retfile
        


def checkFileExpire():
    #filelistss = os.listdir(targetDir)
    filelistss = getsubdir(targetDir)
    #print '------------------'
    #print filelistss
    for filelistt in filelistss:
        filelists = getsubdir(filelistt, True)
        #print filelists
        
        filelist = filter(lambda x: os.path.isdir(x), filelists)
        print filelist
        #print filelist
        for dirTimes in filelist:
            dirTime =  os.stat(dirTimes).st_mtime
            currentTime = time.time()
            #print '----------------'
            #print dirTime
            #print currentTime
            #print '----------------'
            if currentTime - dirTime > expireTime:
                #print 'show delete folder'
                #print True, dirTime
                yield True, dirTimes

    
    
while True:
    for ss, tt in checkFileExpire():
        print 'start delete file over expire time'
        print 'show Flag', ss
        print 'show file',tt
        print '---------------------------------'
        cmd = 'rm -rf %s'%tt
        print cmd
        os.system(cmd)
    time.sleep(runDelay)

#print newest
#checkFileExpire()


