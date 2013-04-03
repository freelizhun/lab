import zmq
import sys
c = zmq.Context()
s = c.socket(zmq.REP)
s.bind("tcp://127.0.0.1:6000")
    
while True:
    msg = s.recv()
    print 'Got server2',msg
    s.send(msg)
