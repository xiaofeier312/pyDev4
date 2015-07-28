#encoding:utf-8
'''
Created on 2015年7月28日

@author: Zhijun.Zhou
'''
import json
import requests
import unittest
from AllCases.common.common import common

class queryPayOrder(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://192.168.9.128:8342/ebk-commission-api/payOrder/queryPayOrder'
        self.data = {"hotelId":"52407003"}
        self.jdata = json.dumps(self.data)
        self.loginHeader = {'content-type':'application/json'}

    def tearDown(self):
        pass
    
    def testQueryOrder(self):
        tempCookie = common().getAssembleKeyInCookieInPortal()
        self.req = requests.post(self.URL, data = self.jdata, cookies = tempCookie, headers = self.loginHeader)
        print self.req.status_code 
        print "Get response:~~~~  ", self.req.content
        self.assertEquals(self.req.status_code, 200, "not back 200")
        
if __name__ == '__main__':
    unittest.main