from wsgiref.simple_server import make_server
import app
httpd = make_server('', 8888, app.dispatch_app)
httpd.serve_forever()
