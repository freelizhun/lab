import httplib
import json


def getToken(token = None, message=None):
    params ='{}'
    headers = {"Content-Type": "application/json"}
    method = "GET"
    path="/cgi-bin/gettoken?corpid=wx2ebd57290f8af1ad&corpsecret=aZh8165A1qP7ltq858y0iDkIJisgaVwzpuaLdVURKIs6bMp7Tna950Dty4DvZHcN"
    print path
    http_port = '443' # '5000'
    #http_ip = "https://qyapi.weixin.qq.com"
    http_ip = "qyapi.weixin.qq.com"
    status, resp = _httpRequest(method, path, params, http_ip, http_port)
    print ' ----------------  show launch vm result -------------------'
    print resp
    print status
    return resp['access_token']
    #return status

# https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx2ebd57290f8af1ad&corpsecret=aZh8165A1qP7ltq858y0iDkIJisgaVwzpuaLdVURKIs6bMp7Tna950Dty4DvZHcN
def _httpRequest(method, path, params, http_ip, http_port):
    headers = {"Content-Type": "application/json"}
    #conn = httplib.HTTPSConnection("qyapi.weixin.qq.com","443")
    conn = httplib.HTTPSConnection(http_ip,http_port)
    conn.request(method, path, params, headers)
    response = conn.getresponse()
    print response
    print 'show response'
    data = response.read()
    verify_services = json.loads(data)
    conn.close()
    return response.status, verify_services

#token = '6jH7PJLNukazh0mRaH2gu1MoNRwgSdh4TX0G4oNii0lUEJW54nFzZp7NgJdnSvKVWko9oGw4Sym1Cme81mTM6Q'
#message = 'test123'
corpid='test'
corpsecret='test'
getToken(corpid, corpsecret)
