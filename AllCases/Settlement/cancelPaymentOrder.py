#encoding:utf-8
'''
Created on 2015年7月28日

@author: Zhijun.Zhou
'''
import json
import requests
import unittest
from AllCases.common.common import common

class cancelPaymentOrder(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://192.168.9.128:8342/ebk-commission-api/commissionPayment/cancelPaymentOrder'
        self.data = {
    "paymentOrderId": 112212323,
    "hotelId": "03201374",
    "operatorId": "15",
    "operatorName": "陶永红",
    "operateIp": "192.168.1.1"
}
        self.jdata = json.dumps(self.data)
        self.loginHeader = {'content-type':'application/json'} 
        
    def tearDown(self):
        pass
    
    def testCancelPaymentOrder(self):
        tempCookie = common()
        self.req = requests.post(self.URL, data = self.jdata, cookies = tempCookie.getAssembleKeyInCookieInPortal(), headers = self.loginHeader)
        print self.req.status_code
        print self.req.content
        self.assertEquals(self.req.status_code, 200, 'return is not 200')
        
if __name__ == '__main__':
    unittest.main
    
    