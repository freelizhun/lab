import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
from tornado import gen
import redis

r = redis.Redis('10.90.1.125')
ps_obj = r.pubsub()

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
  @gen.coroutine
  @gen.engine
  def open(self, room='root'):
    print room
    print 'connection opened...'
    self.write_message("The server says: 'Hello'. Connection was accepted.")

  @gen.coroutine
  @gen.engine
  def on_message(self, message):
    substring='###sub###'
    """
    if substring in message:
        print 'subscribe now'
        ps_obj.subscribe('11111')
        for item in ps_obj.listen():
          print item['data']
          message = str(item['data'])
          print message
          self.write_message("The server says: " + message + " back at you")
    print 'received:', message
    """
    self.write_message("The server says: " + message + " back at you")
    #self.send('haha')

  def on_close(self):
    print 'connection closed...'

application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])


if __name__ == "__main__":
  application.listen(9090)
  tornado.ioloop.IOLoop.instance().start()
