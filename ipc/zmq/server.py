import zmq
import sys
c = zmq.Context()
s = c.socket(zmq.REP)
s.bind('ipc:///tmp/logator.pipe')

print "waiting for workers"
for line in sys.stdin:
    msg = s.recv(copy=False)
    s.send(line)
    
while True:
    msg = s.recv(copy=False)
    s.send('')
