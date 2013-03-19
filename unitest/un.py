import unittest

class EchoTest(unittest.TestCase):  
    def testfoo(self):
        print 'testfoo'
        self.assertTrue(1==2)
        self.assertTrue(1==1)

    #def testbar(self):
    #    print 'testbar'
    #    self.assertTrue(1==1)

#suite = unittest.TestLoader().loadTestsFromTestCase(TestEcho)
#unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()
