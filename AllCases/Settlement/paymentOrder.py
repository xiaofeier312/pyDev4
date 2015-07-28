#encoding:utf-8

'''
Created on 2015年7月28日

@author: Zhijun.Zhou
'''
import unittest
import json
import requests
from AllCases.common.common import common

class paymentOrder(unittest.TestCase):
    '''
                        提交在线付款验证
    '''
    def setUp(self):
        self.URL= 'http://192.168.9.128:8342/ebk-commission-api/commissionPayment/paymentOrder'
        self.data = {
    "hotelId": "03201374",
    "operatorId": "15",
    "operatorName": "陶永红",
    "operateIp": "192.16.1.1",
    "amountTotal": 24.4,
    "paymentorderDetailRequestList": [
        {
            "yearMonth": "2015-07-01 00:00:00",
            "amount": 12.2
        },
        {
            "yearMonth": "2015-07-01 00:00:00",
            "amount": 12.2
        }
    ]
}
        self.jdata = json.dumps(self.data)
        self.loginHeader = {'content-type':'application/json'} 
    
    def tearDown(self):
        pass
    
    def testPaymentOrder(self):
        tempCookie = common()
        self.req = requests.post(self.URL,data = self.jdata, headers = self.loginHeader, cookies = tempCookie.getAssembleKeyInCookieInPortal())
        print "Get response:~~~~  ", self.req.content
        self.assertEquals(self.req.status_code,200)
        
        
if __name__ == '__main__':
    unittest.main
        
