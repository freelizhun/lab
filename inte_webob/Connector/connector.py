

import commands
class Connector:
    def __init__(self):
        self.location = 'this is connector'

    def printData(self):
        print 'haha %s'%self.location
    def writeData(self, uid, data, checksum):
        commands.getoutput('rm -rf /tmp/%s'%uid)
        commands.getoutput('mkdir /tmp/%s'%uid)
        manifestfile = 'a.txt'
        commands.getoutput('touch /tmp/%s/%s'%(uid, manifestfile))
        chunkfilename = '/tmp/'+uid+'/'+checksum
        commands.getoutput('echo %s >> /tmp/%s/%s'%(chunkfilename, uid, manifestfile))
        path='/tmp/%s/%s'%(uid, checksum)
        f = open(path, "w")
        f.write(data)
        f.close()
        return 'ok'
    def readMeta(self, uid):
        manifestfile = 'a.txt'
        ret = commands.getoutput('cat /tmp/%s/%s'%(uid, manifestfile)).split('\n')
        print ret
        return ret
    def commit(self):
        print 'file commit'
        return 'ok'

