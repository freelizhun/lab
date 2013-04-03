import eventlet
import random

global count
post_id=[]
last_id=0

def download(post_id):
    global count
    print "coroutines :",post_id
    sl=random.randint(0,10)
    eventlet.sleep(seconds=sl)
    if count<last_id:
        count=count+1
        q.put(count) # put new coroutines  in the queue

print 'create pool'
pool = eventlet.GreenPool()
q = eventlet.Queue()

print 'append'
for i in range(100,200):
    post_id.append(i)

print 'put'
for i in range(0,5):
    q.put(post_id[i]) # keep 6 coroutines  in the pool

count=post_id[5]
last_id=200

print 'running'
#while not q.empty():
#    print 'run queue'
#    pool.spawn_n(download, q.get())
#    if q.empty(): pool.waitall()
    #if q.empty(): pool.waitall()
while not q.empty() or pool.running()!=0:
    pool.spawn_n(download,q.get()) #start corroutines

print "The end" #nerver reach to this line
