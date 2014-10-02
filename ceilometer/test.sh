
token='90872f53cf534bf98292693ffe31c1ac'

curl -H "X-Auth-Token: $token" -H 'Content-Type: application/json' http://localhost:8777/v2/meters/network.incoming.packets/statistics

