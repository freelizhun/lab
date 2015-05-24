
from nose.tools import ok_, eq_, assert_equal
import time
from testconfig import config
import utils



class TestSuite:
    @classmethod    
    def setupClass(self):
        print '-------  testread1.py ----------'
        print 'prepare stuffs'
        self.token = utils.getToken()
        time.sleep(10)
        
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

    def atest_mult2(self):
        pass
        #eq_(2*2,4)
