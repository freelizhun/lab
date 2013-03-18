class FileIterable(object):
    def __init__(self, count, size=4096):
       print '---into fileiter----'
       self.count = count
       self.chunk_size = size
       #print self.count
    def __iter__(self):
       return FileIterator(self.count, self.chunk_size)
class FileIterator(object):
    #chunk_size = 4096
    def __init__(self, count, chunk_size):
        print '----into tor----'
        self.count = count
        self.chunk_size = chunk_size
        #self.fileobj = open(self.count, 'rb')
    def __iter__(self):
        return self
    def next(self):
        #chunk = self.fileobj.read(self.chunk_size)
        #print self.count
        self.count = self.count + 1
        if self.count > 10:
           print 'count stop'
           raise StopIteration
        return self.count
#def make_response(count):
#    res = Response(content_type=get_mimetype(count))
#    res.app_iter = FileIterable(count)
#    res.content_length = os.path.getsize(count)
#    return res


