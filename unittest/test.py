

import unittest
import func
class CalTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(func.calc(1,2), 3)
        self.assertEqual(func.calc(2,2), 4)



if __name__=='__main__':
    unittest.main()
        
    
