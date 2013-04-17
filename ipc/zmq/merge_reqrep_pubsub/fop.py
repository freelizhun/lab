import zmq
import sys
import time
c = zmq.Context()
s = c.socket(zmq.REQ)
#s.bind("tcp://127.0.0.1:5000")
s.connect('tcp://127.0.0.1:5001')
msg = 'haha'    
while True:
    print 'Got server3',msg
    s.send(msg)
    time.sleep(2)
    aa = s.recv()
    print aa
