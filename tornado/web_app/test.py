import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import os
import string
from time import sleep
from datetime import datetime
import hashlib
import json

from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #print ' return Hello World'
        login_response = {
            'error': True, 
            'msg': 'Thank You.'
        }
        self.write(json.dumps(login_response))

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        email_address = self.get_argument('email', '')
        password = self.get_argument('password', '')

        if not email_address:
            login_response = {
                'error': True, 
                'msg': 'Please enter your email address.'
            }
        elif not password:
            login_response = {
                'error': True, 
                'msg': 'Please enter your password.'
            }
        else:
            login_response = {
                'error': True, 
                'msg': 'Thank You.'
            }

        self.write(login_response)



def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
