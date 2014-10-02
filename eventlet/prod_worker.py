from eventlet.queue import Queue
import eventlet
q = Queue()

def worker():
    while True:
        q.get()
        a = 0
        for i in xrange(1000000):
            a = a + 1
        print 'get'

def producer():
    while True:
        a = 0
        for i in xrange(1000000):
            a = a + 1
        q.put('lol')
        
        print 'put'
        

eventlet.spawn(worker)
eventlet.spawn(producer)
eventlet.sleep(30)

