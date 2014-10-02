from eventlet.queue import Queue
import eventlet
import thread
from eventlet import tpool
q = Queue()

def worker(start):
    while True:
        q.get()
        a = 0 
        for i in xrange(1000000):
            a = a + 1 
        print 'get'

def producer(start):
    print start
    while True:
        print 'haha'
        a = 0 
        for i in xrange(1000000):
            a = a + 1 
        q.put('lol')
    
        print 'put'
    
tpool.execute(worker, thread.get_ident())
tpool.execute(producer, thread.get_ident())
#eventlet.spawn(worker)
#eventlet.spawn(producer)
eventlet.sleep(30)
