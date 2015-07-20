#encoding:utf-8
'''
Created on Jul 19, 2015

@author: light
'''
import unittest
import random


class ChangePrice(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        print "!!!!!testcase2" , random.randint(1,15)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'ChangePrice.testName']
    unittest.main()