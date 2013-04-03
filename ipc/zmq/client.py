import zmq
c = zmq.Context()
s = c.socket(zmq.REQ)
#s.connect('tcp://127.0.0.1:10001')
s.connect('ipc:///tmp/logator.pipe')

while True:
    s.send('sss', copy=False)
    line = s.recv(copy=False)
    if line == '': break
    print line
