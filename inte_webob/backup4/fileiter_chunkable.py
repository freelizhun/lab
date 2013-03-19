class FileIterable(object):
    def __init__(self, filename, size=4096):
       self.filename = filename
       self.chunk_size = size
    def __iter__(self):
       return FileIterator(self.filename, self.chunk_size)
class FileIterator(object):
    #chunk_size = 4096
    def __init__(self, filename, chunk_size):
        self.filename = filename
        self.chunk_size = chunk_size
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

