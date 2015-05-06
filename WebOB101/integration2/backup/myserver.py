from wsgiref.simple_server import make_server
import eventlet
from eventlet import wsgi
from paste.deploy import loadapp
import os


app = loadapp('config:%s' % os.path.abspath('paste.ini'))
httpd = make_server('localhost', 8282, app)
httpd.serve_forever()
