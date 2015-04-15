#!/usr/bin/env python

import collectd
import redis


CONFIGS = []


def config(conf):

    collectd.info('------ config ------')

    for node in conf.children:
        key = node.key.lower()
        val = node.values[0]
        if key == 'host':
            host = val
        elif key == 'port':
            port = int(val)
        elif key == 'db':
            db = int(val)
        elif key == 'key':
            key = val
        else:
            collectd.warning('redis_info plugin: Unknown config key: %s' % key)
            continue

    CONFIGS.append({
        'host': host,
        'port': port,
        'db': db,
        'key': key,
    })


def read():

    collectd.info('------ read ------')

    for conf in CONFIGS:

        rdb = redis.StrictRedis(host=conf['host'], port=conf['port'], db=conf['db'])
        value = rdb.llen(conf['key'])
        val = collectd.Values(plugin='redis_info')
        val.type = 'gauge'
        val.type_instance = conf['key']
        val.values = [value]
        val.dispatch()


collectd.register_config(config)
collectd.register_read(read)
