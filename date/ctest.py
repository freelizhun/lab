

import time


class testdd():
    def __init__(self):
        self.test = 'hahha'

    def run_once(self):
        print self.test

    def run_forever(self):
        while True:
            self.run_once()
            time.sleep(10)



