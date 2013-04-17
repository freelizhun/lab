import zmq
import sys
from random import choice
c = zmq.Context()
s = c.socket(zmq.PUB)
s.bind("tcp://127.0.0.1:5000")
countries = ['aa','bb','cc','dd']    
events = ['11','22','33','44']    
while True:
    msg = choice(countries)+' '+choice(events)
    s.send(msg)
