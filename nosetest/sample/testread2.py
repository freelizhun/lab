
from nose.tools import ok_, eq_, assert_equal
import time
from testconfig import config
import utils
from . import token


class TestSuite:
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
        
    def test_mult(self):
        print 'token in stuff %s'%self.token
        #eq_(2*2,4)
        #assert_equal('201','200','correct')
        self.mult1()
        assert_equal('201','200','test 1')
        self.failignored()
        assert_equal('200','200','test 2')
        self.mult1()
        assert_equal('200','200','test 3')
        
    def mult1(self):
        eq_(2*2,4)

    def failignored(self):
        return 'haha'

    def test_mult2(self):
        eq_(2*2,4)
        #eq_(2*2,4)
