import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
#s.connect('tcp://127.0.0.1:10001')
#socket.connect('tcp://127.0.0.1:5000')
#socket.connect('tcp://127.0.0.1:6000')
socket.bind("tcp://127.0.0.1:5000")

for i in range(10):
    msg='msg client2 %s'%i
    socket.send(msg)
    print 'sending',msg
    msg_in = socket.recv()
    print msg_in
