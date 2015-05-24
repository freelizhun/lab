
from nose.tools import ok_, eq_, assert_equal
import time
from testconfig import config
import utils
from . import token


class TestSequence:
    """        
    def setup(self):
        print 'prepare stuffs'
        self.token = token
        #self.token = utils.getToken()
        time.sleep(10)
    """
    @classmethod
    def setupClass(self):
        print '------- into testread2 -----'
        self.token = token
        

    def test_3_haha3(self):
        print '-------3'
        eq_(2*2,4)

    def test_2_haha2(self):
        print '-------2'
        eq_(2*2,4)

    def test_5_haha5(self):
        print '-------5'

    def test_0_mult(self):
        print '-------0'
        print 'token in stuff %s'%self.token
        eq_(2*2,4)

    def test_4_haha4(self):
        print '-------4'
        eq_(2*2,4)

    def test_1_haha(self):
        print '-------1'
        eq_(2*2,4)



