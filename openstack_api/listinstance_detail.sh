curl -s -X GET -H "X-Auth-Token: $TOKEN" -H "Content-Type: application/json" http://192.168.1.102:8774/v2/d04021d5a4144b4c9f579fdc1d1c2a9a/servers/detail|python -m json.tool
