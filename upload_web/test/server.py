from webob import Request
from webob import Response
class ChunkApp(object):
    def __init__(self):
        pass
    def __call__(self, environ, start_response):
        req = Request(environ)

        for buf in self.chunkreadable(req.body_file, 65535):
            print buf

        resp = Response('chunk received')
        return resp(environ, start_response)
    def chunkreadable(self, iter, chunksize=65536):
        return self.chunk(iter, chunk_size) if \
                hasattr(iter, 'read') else iter

    def chunkiter(self, fp, chunksize=65536):
        while True:
            chunk = fp.read(chunk_size)
            if chunk:
                yield chunk
            else:
                break
if __name__=='__main__':
    app = ChunkApp()
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost',8080, app)
    try:
        httpd.serve_forever()
    except keyboardInterrupt:
        print '^C'
