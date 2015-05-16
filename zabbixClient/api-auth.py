#coding=utf-8
import json
#import urllib3 as urllib2
import urllib2
#from urllib3 import request, urlopen, URLError, HTTPError

# based url and required header
url = "http://172.16.235.128/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# auth user and password
data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
    "user": "Admin",
    "password": "zabbix"
},
"id": 0
})
# create request object
request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
# auth and get authid
result = urllib2.urlopen(request)
#print "Auth Failed, Please Check Your Name And Password:",e.code
response = json.loads(result.read())
result.close()
print "Auth Successful. The Auth ID Is:",response['result']

