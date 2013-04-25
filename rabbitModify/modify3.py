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
#conn.putrequest("POST", "/?file=save.jpg")
conn.putrequest("GET", "/v1/modify")
#conn.putheader("Content-Type", "application/zip")
conn.putheader("Content-Type", "application/json")
conn.putheader("X-Meta-Notify", "test")
conn.endheaders()
 
response = conn.getresponse()
print response.status
print 'left modify 2'
