import eventlet
import time
a=0
try:
    with eventlet.timeout.Timeout(5):
        while True:
            a = a+1
except eventlet.Timeout:
    print 'time out'
