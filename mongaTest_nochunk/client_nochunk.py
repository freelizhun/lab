import httplib
import sys
import mimetypes
import os
import commands
import time
#CHUNKSIZE = 65563  
CHUNKSIZE = 4096
fp='/root/small.txt'
#CHUNKSIZE = 6
url="http://127.0.0.1:8090/"
conn = httplib.HTTPConnection("127.0.0.1", 8090)
#conn.putrequest("POST", "/?file=save.jpg")
#conn.putrequest("POST", "/?file=save.jpg")
conn.putrequest("PUT", "/test")
#conn.putheader("Content-Type", "application/zip")
conn.putheader("Content-Type", "application/json")
fsize =int( commands.getoutput('ls -al %s'%fp).split()[4]) -1024000
conn.putheader("Content-Length", str(fsize))

#conn.putheader("Content-Length", "3000000")
#conn.putheader("Transfer-Encoding", "chunked")
conn.putheader("Filepath","/tmp/huge/h.txt")
conn.endheaders()
 
#fp = '/root/random.zip'
#fp = './zero.txt'
#fp = './ddd.jpg'
#fp = './size.txt'
#fp='./random.txt'
# fp = 'C:\Users\haow\Downloads\MONACO.TTF'
f = os.path.basename(fp)
f = fp
print f
print mimetypes.guess_type(f)
with open(f, 'r') as fp:
     chunk = fp.read(CHUNKSIZE)
     #print chunk
     while chunk:
         conn.send('%x\r\n%s\r\n' % (len(chunk), chunk))
         chunk = fp.read(CHUNKSIZE)
         #time.sleep(1)
     conn.send('0\r\n\r\n')
print 'send over'
response = conn.getresponse()
print response.read()
