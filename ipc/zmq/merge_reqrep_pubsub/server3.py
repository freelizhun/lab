import zmq
import sys
import time
c = zmq.Context()
s = c.socket(zmq.REP)
#s.bind("tcp://127.0.0.1:5000")
s.connect('tcp://127.0.0.1:5000')
    
while True:
    msg = s.recv()
    print 'Got server3',msg
    s.send(msg)
    time.sleep(2)
