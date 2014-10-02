import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
 
GB = 1024 * 1024 * 1024
body_size = 1 * GB
 
 
class StreamingRequestHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        total_sent = 0
        chunk = 'a' * 1024 * 1024 
 
        self.set_header('Content-Length', body_size)
        while total_sent < body_size:
            print 'into'
            #yield gen.Task(self.write, chunk)
            self.write(chunk)
            #self.flush(include_footers=False, callback=(yield tornado.gen.Callback('self.flush')))
            #yield gen.Task(self.flush(include_footers=False))
            print 'ready to flush'
            yield gen.Task(self.flush, include_footers=False)
            total_sent += len(chunk)
            print 'sent', total_sent / float(GB), 'GB'
            print 'sent1', total_sent / float(GB)*1024, 'MB'
        print 'left'
        self.flush() 
        self.finish()
 
 
if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", StreamingRequestHandler),
    ])
    application.listen(8811)
    tornado.ioloop.IOLoop.instance().start()

