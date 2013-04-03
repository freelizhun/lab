import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
#s.connect('tcp://127.0.0.1:10001')
socket.connect('tcp://127.0.0.1:5000')
socket.setsockopt(zmq.SUBSCRIBE,'aa')
while True:
    print 'server1',socket.recv()
        
