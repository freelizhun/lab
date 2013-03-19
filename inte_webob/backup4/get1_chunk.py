import httplib, urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
#url = 'http://localhost:8090/search?q=haha&aq=f'

conn = httplib.HTTPConnection("localhost:8090")
conn.request("GET", "/cgi-bin/query", params, headers)
response = conn.getresponse()
print response.status, response.reason


#print data
#conn.close()
f = open('./download1.jpg',"wb")
chunksize = 4096000
data = response.read(chunksize)
while data:
    f.write(data)
    data = response.read(chunksize)
f.close()
conn.close()
