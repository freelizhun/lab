import eventlet
from eventlet import wsgi
from eventlet import GreenPool
from paste.deploy import loadapp

import os
#eventlet.patcher.monkey_patch(all=False, socket=True)
eventlet.patcher.monkey_patch(os=True, select=True, socket=True, thread=False, time=True)
app = loadapp('config:%s' % os.path.abspath('proxy.conf'))
pool =GreenPool(size=1024)
wsgi.server(eventlet.listen(('', 8090)), app, custom_pool=pool)
pool.waitall()

