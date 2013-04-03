import zmq
import sys
c = zmq.Context()
s = c.socket(zmq.REP)
s.bind("tcp://127.0.0.1:5000")
    
while True:
    msg = s.recv()
    print 'Got server1',msg
    s.send(msg)
