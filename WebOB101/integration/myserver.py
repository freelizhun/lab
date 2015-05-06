import eventlet
from eventlet import wsgi
from paste.deploy import loadapp
import os
app = loadapp('config:%s' % os.path.abspath('paste.ini'))
wsgi.server(eventlet.listen(('', 8090)), app)

