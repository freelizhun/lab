from eventlet import Timeout
import eventlet

try:
    with Timeout(3):
        a = 0
        while True:
            a = a + 1
            if a<0:
                break
except (Exception, Timeout):
    print 'time out'

