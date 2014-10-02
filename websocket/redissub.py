import redis
import sys
r = redis.Redis('10.90.1.125')
ps_obj = r.pubsub()
ps_obj.subscribe('aa')

for item in ps_obj.listen():
    print item['data']
