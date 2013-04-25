

import commands
class Connector:
    def __init__(self):
        self.location = 'this is connector'
        #commands.getoutput('rm -rf /tmp/aaa')

    def printData(self):
        print 'haha %s'%self.location
    def writeData(self, uid, fname, data, checksum):
        path = fname.rsplit('/',1)[0]
        commands.getoutput('mkdir %s'%path)
        manifestfile = fname
        commands.getoutput('touch %s'%(manifestfile))
        chunkfilename = path+'/'+checksum
        commands.getoutput('echo %s >> %s'%(chunkfilename, manifestfile))
        path='%s/%s'%(path, checksum)
        f = open(path, "w")
        f.write(data)
        print 'write data %s'%len(data)
        f.close()
        return 'ok'
    def readMeta(self, uid):
        manifestfile = uid
        ret = commands.getoutput('cat %s'%(manifestfile)).split('\n')
        print ret
        return ret
    def commit(self):
        print 'file commit'
        return 'ok'

