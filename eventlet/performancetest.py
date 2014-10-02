import eventlet
import random
import time
import uuid
import commands
import httplib
total = 1000
filesize = 1024*1024*3
concurrency=300
keystoneIP='10.90.0.52'
fcip='localhost'




eventlet.patcher.monkey_patch(socket=True)
pool = eventlet.GreenPool(concurrency)

global source
lower_object_size = 100
upper_object_size = 100
#source = SourceFile(random.randint(lower_object_size,
#                               upper_object_size))
#source = 'asdfasdfasdfas'*10000000
source = 'a'*filesize
global failure
failure = 0
global success
success = 0
print len(source)
#print source


def getTokenTid(user, password):
    global keystoneIP
    s ="""curl -X POST -v -H 'Content-Type: application/json' %s:35357/v3/auth/tokens -d '{"auth":{"identity":{"methods":["password"],"password":
        {"user":{"domain":{"name":"cs.promise.com.tw"},"name":"%s","password":"%s"}}},"scope":{"project":{"domain":{"name":"cs.promise.com.tw"},"name":"%s"}}}}'"""%(keystoneIP, user,password,user)
    strr = commands.getoutput(s)
    ss= strr.split('left intact')
    token =  ss[0].split('X-Subject-Token:')[1].split()[0]
    return token
global token
token = getTokenTid('Carol.Wilson','Password1')




def sendfile():
    #print 'send file'
    global token
    global source


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
    #print 'response:',response.status
    if response.status == 200:
        return '200'
    else:
        return '400'
    
    
    
def _run(thread):
    global failure
    global success
    #print 'test'
    #eventlet.sleep(1)
    #sendfile()
    res = sendfile()
    #print res
    if res!='200':
        failure += 1
        return 
    else:
        success += 1
        return 


inittime = time.time()
for i in xrange(total):
    pool.spawn_n(_run, i)
pool.waitall()
fintime = time.time()
res =  fintime-inittime

print 'total time:',res
print 'filesize(Bytes):',len(source)
print 'average latency:',res/(success - failure)
print 'thouput(MB/s):',success*len(source)/res/(1024.*1024.)
print 'success',success
print 'failure',failure




