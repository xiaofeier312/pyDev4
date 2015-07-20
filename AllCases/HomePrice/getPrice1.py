#encoding:UTF8

import unittest
import random

class GetPrice1(unittest.TestCase):
    def setUp(self):
        print "this is setUP"
        self.seq  = range(10)
        print self.seq
        
    def setDown(self):
        print "this is setUP"
        
    def testGetPrice(self):
        self.key = random.randint(2,22)
        print "key is",self.key
        self.assertTrue(self.key in self.seq, "msg!!1")
        

if __name__ == "__main__":
    unittest.main()      