import httplib, urllib
import json
#url = 'http://localhost:8090/search?q=haha&aq=f'
import sys
sys.setrecursionlimit(100)
global token
token ='2d1f04222eec4331ab44b378936528f1'

def delete(fdir):
    global token

    url="http://127.0.0.1:7000/"
    ufdir =unicode(fdir).encode('utf8')
    print ufdir
    conn = httplib.HTTPConnection("127.0.0.1", 7000)
    conn.putrequest('POST', '/v1/fileops/delete?path=%s'%ufdir) 
    conn.putheader("X-AUTH-Token","%s"%token)
    conn.endheaders()

    response = conn.getresponse()
    print '------status--------'
    print response.status
    print '------resaon--------'
    print response.reason
    print '----- read -------'
    ret= response.read()
    print ret 
    retd= json.loads(ret)
    print retd
    return retd


def getmeta(fdir=None):
    global token
    conn = httplib.HTTPConnection("localhost:7000")
    if fdir:
        conn.putrequest("GET", "/v1/metadata/%s"%fdir)
    else:
        conn.putrequest("GET", "/v1/metadata")
    conn.putheader("X-AUTH-Token","%s"%token)
    conn.endheaders()
    response = conn.getresponse()
    #print response.status, response.reason

    #print '------status--------'
    #print response.status
    #print '------resaon--------'
    #print response.reason
#print '----- read -------'
#print response.getheader('x-dropbox-metadata')
    ret= response.read()
#print ret
    retd= json.loads(ret)
    #print retd
    rrs = retd.get('contents')
    #rrs.pop('/shared')
    return rrs

def getFolderInfo(fdir):
    ret = getmeta(fdir)
    for re in ret:
        print 'subpath',re.get('path')
        if re.get('is_dir'):
            ret = getFolderInfo(re.get('path'))
            print 'sub delete folder:',fdir
            delete(re.get('path'))
        else:
            print 'sub delete %s'%(re.get('path'))
            delete(re.get('path'))
    return fdir
    
    

rrs = getmeta()
#rrs = retd.get('contents')
print '--------------------'
print rrs
print '--------------------'

for ret in rrs:
    print ret.get('is_dir'),ret.get('bytes'),ret.get('path')
    if ret.get('path')!='/shared':
        if ret.get('is_dir'):
            print ret.get('path')
            fret = getFolderInfo(ret.get('path'))
            print 'delete folder',ret
            delete(ret.get('path'))
        else:
            print 'delete'
            delete(ret.get('path'))
