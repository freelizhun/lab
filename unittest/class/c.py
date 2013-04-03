import random
import unittest
import time

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print 'first'
        self.seq = range(10)

    def test_shuffle(self):
        print '1'
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        print '2'
        element = random.choice(self.seq)
        time.sleep(5)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        print '3'
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
class TestSequenceFunctions1(unittest.TestCase):

    def setUp(self):
        print 'second'
        self.seq = range(10)

    def test_shuffle(self):
        print '11'
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        print '22'
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        print '33'
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
