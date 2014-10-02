import httplib2
from urllib import urlencode
h = httplib2.Http()
 
## Add articles
data = {'id':'1', 'author':'B', 'genre':'comedy'}
body = urlencode(data)
h.request("http://127.0.0.1:8888/articles", "POST", body=body)
 
data = {'id':'1', 'author':'C', 'genre':'comedys'}
body = urlencode(data)
h.request("http://127.0.0.1:8888/articles", "POST", body=body)

data = {'id':'2', 'author':'A', 'genre':'tragedy'}
body = urlencode(data)
h.request("http://127.0.0.1:8888/articles", "POST", body=body)

data = {'id':'3', 'author':'X', 'genre':'tragedy'}
body = urlencode(data)
h.request("http://127.0.0.1:8888/articles", "POST", body=body)
 
## View all articles
content, response = h.request("http://127.0.0.1:8888/articles", "GET")
print '------- all articles -------'
print  response
## View articles
print '------- per articles -------'
data = {"articleid":1}
data = urlencode(data)
content, response = h.request("http://127.0.0.1:8888/articles"+ "?" + data, "GET")
#for res in response:
#    print res
print  response
 
## Delete articles
#content, response = h.request("http://127.0.0.1:8888/articles", "DELETE")
 
#content, response = h.request("http://127.0.0.1:8888/articles", "GET")
#print  response
