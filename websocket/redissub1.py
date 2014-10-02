import redis
import sys
def on_messages_published(message):
    print message

r = redis.Redis('10.90.1.125')
ps_obj = r.pubsub()
ps_obj.subscribe('aa')
ps_obj.listen(on_messages_published)
#for item in ps_obj.listen():
#    print item['data']

