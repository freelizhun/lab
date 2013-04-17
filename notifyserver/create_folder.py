import httplib
import sys
import mimetypes
import os
import json
#CHUNKSIZE = 65563  
CHUNKSIZE = 4096
#CHUNKSIZE = 6
url="http://127.0.0.1:8090/"
conn = httplib.HTTPConnection("127.0.0.1", 8090)
#conn.putrequest("POST", "/?file=save.jpg")
#conn.putrequest("POST", "/?file=save.jpg")
#conn.putrequest("PUT", "/test?file=haha")
#conn.putrequest("POST", "/fileops", body)
#conn.putheader("Content-Type", "application/zip")
#conn.putheader("Content-Type", "application/json")
#conn.putheader("Transfer-Encoding", "chunked")
##conn.putheader("Filepath","/tmp/size/s.txt")
#conn.endheaders(body)

body = json.dumps({'test1':'test11','test2':'test22'})

conn.request('POST', '/fileops', body=body, headers={}) 
#fp = '/root/random.zip'
#fp = './zero.txt'
#fp = './ddd.jpg'
#fp = './size.txt'
fp='./size.txt'
#fp='./random.txt'
# fp = 'C:\Users\haow\Downloads\MONACO.TTF'
f = os.path.basename(fp)
#print f
#print mimetypes.guess_type(f)
#with open(f, 'r') as fp:
#     chunk = fp.read(CHUNKSIZE)
     #print chunk
#     while chunk:
#         conn.send('%x\r\n%s\r\n' % (len(chunk), chunk))
#         chunk = fp.read(CHUNKSIZE)
#     conn.send('0\r\n\r\n')
response = conn.getresponse()
#response = getresponse()
print '------status--------'
print response.status
print '------resaon--------'
print response.reason
print '----- read -------'
#ret= response.read()
#print ret
#retd= json.loads(ret)
#print retd
#print response.headers


