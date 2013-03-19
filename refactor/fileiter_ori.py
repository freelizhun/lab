class FileIterable(object):
    def __init__(self, filename):
       self.filename = filename
    def __iter__(self):
       return FileIterator(self.filename)
class FileIterator(object):
    chunk_size = 4096
    def __init__(self, filename):
        self.filename = filename
        self.fileobj = open(self.filename, 'rb')
    def __iter__(self):
        return self
    def next(self):
        chunk = self.fileobj.read(self.chunk_size)
        if not chunk:
           raise StopIteration
        return chunk
#def make_response(filename):
#    res = Response(content_type=get_mimetype(filename))
#    res.app_iter = FileIterable(filename)
#    res.content_length = os.path.getsize(filename)
#    return res

