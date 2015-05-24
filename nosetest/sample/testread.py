
from nose.tools import ok_, eq_, assert_equal
from nose.tools import timed
import time
from testconfig import config
import utils
from . import token



class TestSuite:
    """    
    # every testcase will execute this
    def setup(self):
        print 'into setup'
        self.token = utils.getToken()
    """
    #execute once
    @classmethod
    def setupClass(self):
        #global token
        print 'into setup'
        print 'inittial variable %s'%token
        self.token = token
        #self.token = utils.getToken()
    
        
    #def teardown(self):
    #    print 'function tear down'
    def test_mult(self):
        print 'token %s'%self.token
        print '0'
        time.sleep(10)
        #eq_(2*2,4)
        #assert_equal('201','200','correct')
        assert_equal('200','200','test 3')

    @timed(2)
    def test_timeout(self):
        print ' into check timeout'
        time.sleep(3)
        
    def test_mult1(self):
        print '1: %s'%self.token
        eq_(2*2,4)

    def test_failignored(self):
        print '2'
    

    def test_mult2(self):
        print '3'
        time.sleep(2)
        eq_(2*2,4)

    def test_0_seq(self):
        print 'seq 0'
        eq_(2*2,4)

    def test_2_seq(self):
        print 'seq 2'
        eq_(2*2,4)

    def test_1_seq(self):
        print 'seq 1'
        eq_(2*2,4)

