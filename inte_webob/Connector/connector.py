

import commands
class Connector:
    def __init__(self):
        self.location = 'this is connector'

    def printData(self):
        print 'haha %s'%self.location
    def writeData(self, uid, data, checksum):
        commands.getoutput('mkdir /tmp/%s'%uid)
        manifestfile = 'a.txt'
        commands.getoutput('touch /tmp/%s/%s'%(uid, manifestfile))
        commands.getoutput('echo %s >> /tmp/%s/%s'%(checksum, uid, manifestfile))
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

