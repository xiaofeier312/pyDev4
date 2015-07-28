#encoding:utf-8
'''
Created on 2015年7月28日

@author: Zhijun.Zhou
'''
import unittest
import requests
import json
from AllCases.common.common import common

class debtUnPayment(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://192.168.9.128:8342/ebk-commission-api/commissionPayment/debtUnPayment'
        self.data = {
    "hotelId": "03201374",
    "operatorId": "15",
    "operatorName": "陶永红",
    "operateIp": "192.168.1.1",
    "noPayInfo": "临时有事"
}       
        self.jdata = json.dumps(self.data)
        self.loginHeader = {'content-type':'application/json'} 
        
    def tearDown(self):
        pass
    
    def testDebtUnpayment(self):
        tempCommon = common()
        result = requests.post(self.URL, data = self.jdata, headers = self.loginHeader, cookies = tempCommon.getAssembleKeyInCookieInPortal())
        print result.status_code
        print result.raw
        print "Get response:~~~~  ", result.content
        print result.headers
        print result.cookies
        print result.history
        self.assertEquals(result.status_code,200,'return is not 200')
        
if __name__ == '__main__':
    unittest.main
        