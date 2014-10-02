import redis
import sys
r = redis.Redis('10.90.1.125')
r.publish('aa','hahaha')
