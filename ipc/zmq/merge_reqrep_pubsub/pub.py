import zmq
import sys
from random import choice
c = zmq.Context()
s = c.socket(zmq.PUB)
s.bind("tcp://127.0.0.1:5000")
countries = ['aa','bb']    
events = ['11','22','33','44']    

#context = zmq.Context()
socket = c.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5001")





while True:
    rdata = socket.recv()
    print rdata
    socket.send('baby')
    print rdata
    msg = choice(countries)+' '+choice(events)
    s.send(msg)
