curl -si -H"X-Auth-Token:$TOKEN" -H "Content-type: application/json" http://192.168.1.102:9696/v2.0/subnets | tail -1 | python -m json.tool
