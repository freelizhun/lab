import eventlet
import random
import time
import uuid
import commands
import httplib
total = 100
concurrency=10
pool = eventlet.GreenPool(concurrency)
keystoneIP='10.90.0.52'
fcip='localhost'


class SourceFile(object):
    """
    Iterable, file-like object to lazily emit a bunch of zeros in
    reasonable-size chunks.

    swift.common.direct_client wants iterables, but swiftclient wants
    file-like objects where hasattr(thing, 'read') is true. Therefore,
    this class can do both.
    """

    def __init__(self, size, chunk_size=1024 * 64):
        self.pos = 0
        self.size = size
        self.chunk_size = chunk_size

    def __iter__(self):
        return self

    def __len__(self):
        return self.size

    def next(self):
        if self.pos >= self.size:
            raise StopIteration
        chunk_size = min(self.size - self.pos, self.chunk_size)
        yield '0' * chunk_size
        self.pos += chunk_size

    def read(self, desired_size):
        chunk_size = min(self.size - self.pos, desired_size)
        self.pos += chunk_size
        return '0' * chunk_size

global source
lower_object_size = 100
upper_object_size = 100
source = SourceFile(random.randint(lower_object_size,
                               upper_object_size))
global failure
failure = 0
global success
success = 0
print len(source)
print source


def getTokenTid(user, password):
    global keystoneIP
    s ="""curl -X POST -v -H 'Content-Type: application/json' %s:35357/v3/auth/tokens -d '{"auth":{"identity":{"methods":["password"],"password":
        {"user":{"domain":{"name":"cs.promise.com.tw"},"name":"%s","password":"%s"}}},"scope":{"project":{"domain":{"name":"cs.promise.com.tw"},"name":"%s"}}}}'"""%(keystoneIP, user,password,user)
    #print s
    strr = commands.getoutput(s)
    print strr
    ss= strr.split('left intact')
#print ss.get('project')
#print '---------------'
#print ss[0]
    #print '------------------------------------'
    token =  ss[0].split('X-Subject-Token:')[1].split()[0]
    print 'show token ---------------',token
    #t_idtmp= ss[1].split('*')[0].strip()
    #t_id =  json.loads(t_idtmp)['token']['project']['id']
    return token
global token
token = getTokenTid('Carol.Wilson','Password1')
#tenant_id = getTenantid('Carol.Wilson','Password1')




def sendfile():
    global token
    #global source

    source = 'asdfasdfasdfas'

    uploadpath =  uuid.uuid1()

    CHUNKSIZE = 4096 
    url="http://127.0.0.1:7000/"
    conn = httplib.HTTPConnection("%s:7000"%fcip)
    conn.putrequest("POST", "/v1/files/%s?overwrite=true&parent_rev=notyet"%uploadpath)
    conn.putheader("Content-Type", "application/json")
    global token
    conn.putheader("X-Auth-Token","%s"%token)
    conn.putheader("Content-Length", str(len(source)) )
    conn.endheaders()
    counter = 0
    #chunk = source(counter:(counter+CHUNKSIZE))
    #print chunk
    conn.send(source)
    """
    while chunk:
        #conn.send('%x\r\n%s\r\n' % (len(chunk), chunk))
        conn.send('%s' % (chunk))
        counter = counter + chunk
        chunk = source(counter:(counter+CHUNKSIZE))
        #conn.send('0\r\n\r\n')
    """
    response = conn.getresponse()
    print '------status--------'
    print response.status
    print '------resaon--------'
    print response.reason
    print '----- read -------'
    if response.status == '200':
        return '200'
    else:
        return '400'
    
    
    
def _run(thread):
    global failure
    global success
    print thread
    eventlet.sleep(1)
    if sendfile()!='200':
        failure += 1
        return 
    else:
        success += 1
        return 


inittime = time.time()
for i in xrange(total):
    pool.spawn_n(_run, i)
pool.waitall()
print time.time()-inittime
print failure
print success




