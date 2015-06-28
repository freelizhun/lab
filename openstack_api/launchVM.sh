curl -s -X POST -H "X-Auth-Token: $TOKEN" -H "Content-Type: application/json" http://192.168.1.102:8774/v2/d04021d5a4144b4c9f579fdc1d1c2a9a/servers -d '{"server": {"name": "instance1", "imageRef": "a18185af-640c-45d5-9d6e-b47303b19798", "flavorRef": "1", "max_count": 1, "min_count": 1, "networks": [ { "uuid": "ed58fc5d-7bb0-4223-bf94-2387a79d9ffe" } ] }}'

#384
