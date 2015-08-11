import httplib
import json


def sendMessage(token = None, message=None):
    print '------------ launch VM ------------'
    #params = '{"touser": "@all","toparty": "@all","totag":"@all","msgtype":"text","agentid": "2","text":{ "content": %s},"safe":"0"}'%message
    params = '{"touser": "@all","toparty": "@all","totag":"@all","msgtype":"text","agentid": "2","text":{ "content": \"%s\"},"safe":"0"}'%message
    #params =urllib.urlencode({"server":{"name":"instance1", "imageRef": "6e09b461-0ab2-40fb-a182-a3d910adc54e", "flavorRef": "1", "max_count": 1, "min_count": 1}})
    print 'params %s'%params
    headers = {"Content-Type": "application/json"}
    method = "POST"
    path = "/cgi-bin/message/send?access_token=%s"%token
    print path
    http_port = '443' # '5000'
    http_ip = "https://qyapi.weixin.qq.com"
    status, resp = _httpRequest(method, path, params, http_ip, http_port)
    print ' ----------------  show launch vm result -------------------'
    print resp
    print status
    return status

def _httpRequest(method, path, params, http_ip, http_port):
    headers = {"Content-Type": "application/json"}
    conn = httplib.HTTPSConnection("qyapi.weixin.qq.com","443")
    conn.request(method, path, params, headers)
    response = conn.getresponse()
    print response
    print 'show response'
    data = response.read()
    verify_services = json.loads(data)
    conn.close()
    return response.status, verify_services

token = '6jH7PJLNukazh0mRaH2gu1MoNRwgSdh4TX0G4oNii0lUEJW54nFzZp7NgJdnSvKVWko9oGw4Sym1Cme81mTM6Q'
message = 'test123'
sendMessage(token, message)
