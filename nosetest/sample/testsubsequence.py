
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
        

    def test_haha_3(self):
        print '---haha----3'
        eq_(2*2,4)

    def test_haha_2(self):
        print '---haha----2'
        eq_(2*2,4)

    def test_haha_5(self):
        print '---haha----5'

    def test_haha_0(self):
        print '---haha----0'
        print 'token in stuff %s'%self.token
        eq_(2*2,4)

    def test_haha_4(self):
        print '---haha----4'
        eq_(2*2,4)

    def test_haha_1(self):
        print '---haha----1'
        eq_(2*2,4)



    def test_laha_3(self):
        print '---laha----3'
        eq_(2*2,4)

    def test_laha_2(self):
        print '---laha----2'
        eq_(2*2,4)

    def test_laha_5(self):
        print '---laha----5'

    def test_laha_0(self):
        print '---laha----0'
        print 'token in stuff %s'%self.token
        eq_(2*2,4)

    def test_laha_4(self):
        print '---laha----4'
        eq_(2*2,4)

    def test_laha_1(self):
        print '---laha----1'
        eq_(2*2,4)
