import eventlet
import time
clients=100
eventlet.patcher.monkey_patch(socket=True)
pool = eventlet.GreenPool(size=clients)
pile = eventlet.GreenPile(pool)
def do_run(i):
    print 'haha',i
    eventlet.sleep(1)
    return 'test',i
for i in xrange(clients):
    print i
    for client in xrange(clients):
        pile.spawn(do_run, client)

    for result in pile:
        print result
      

