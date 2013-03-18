import urllib
import httplib2

url = 'http://localhost:8090/search?q=haha&aq=f'   
#url = 'http://localhost:8090'   
body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
headers = {'Content-Type': 'application/json'}
#headers = {'Content-Type': 'text/plane'}
http = httplib2.Http()
#Request.blank('/serarch?id=1')
response, content = http.request(url, 'GET', headers=headers, body=urllib.urlencode(body))
print '-----response---------'
print response
print '-----content---------'
print content
f = open('./download.jpg',"w")
f.write(content)
f.close()
