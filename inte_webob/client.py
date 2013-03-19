import httplib
import sys
import mimetypes
import os
#CHUNKSIZE = 65563  
CHUNKSIZE = 4096
#CHUNKSIZE = 6
url="http://127.0.0.1:8090/"
conn = httplib.HTTPConnection("127.0.0.1", 8090)
#conn.putrequest("POST", "/?file=save.jpg")
conn.putrequest("POST", "/?file=save.jpg")
#conn.putheader("Content-Type", "application/zip")
conn.putheader("Content-Type", "application/json")
conn.putheader("Transfer-Encoding", "chunked")
conn.endheaders()
 
#fp = '/root/random.zip'
#fp = './zero.txt'
#fp = './ddd.jpg'
#fp = './size.txt'
fp='./random.txt'
# fp = 'C:\Users\haow\Downloads\MONACO.TTF'
f = os.path.basename(fp)
print f
print mimetypes.guess_type(f)
with open(f, 'r') as fp:
     chunk = fp.read(CHUNKSIZE)
     #print chunk
     while chunk:
         conn.send('%x\r\n%s\r\n' % (len(chunk), chunk))
         chunk = fp.read(CHUNKSIZE)
     conn.send('0\r\n\r\n')
response = conn.getresponse()
print response.read()
