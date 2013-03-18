import httplib, urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
#url = 'http://localhost:8090/search?q=haha&aq=f'

conn = httplib.HTTPConnection("localhost:8090")
conn.request("GET", "/cgi-bin/query", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
#print data
conn.close()
f = open('./download1.jpg',"w")
f.write(data)
f.close()

