
import sys
import time
sys.setrecursionlimit(30) 
global counter
counter = 0
def dig():
    global counter
    if counter > 10:
        return None
    print 'a'
    counter = counter + 1
    print counter
    time.sleep(0.3)
    dig()
    print counter
    print 'finished'
    counter = counter - 1
    print counter


dig()
