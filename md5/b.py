import hashlib
import time
while True:
    mmtest = hashlib.md5()
    mmtest.update(ss)
    print str(mmtest.hexdigest())
    time.sleep(1)

