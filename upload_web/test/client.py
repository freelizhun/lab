from httplib import HTTPConnection
conn = HTTPConnection("localhost:8080")
conn.putrequest('PUT', "/")
body = "1234567890"
conn.putheader('Transfer-Encoding', 'chunked')
conn.endheaders()
conn.send('%x\r\n%s\r\n' % (len(body), body))
conn.send('0\r\n\r\n')
