import httplib, urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {"Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain","Filepath":"/tmp/huge/h.txt"}
#url = 'http://localhost:8090/search?q=haha&aq=f'

conn = httplib.HTTPConnection("localhost:8090")
conn.request("GET", "/test", params, headers)
response = conn.getresponse()
print response.status, response.reason


#print data
#conn.close()
f = open('./download_huge.txt',"wb")
chunksize = 4096
data = response.read(chunksize)
while data:
    f.write(data)
    data = response.read(chunksize)
f.close()
conn.close()
