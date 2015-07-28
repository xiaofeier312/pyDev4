#encoding:utf-8
'''
Created on 2015��7��23��

@author: Zhijun.Zhou
'''
import unittest
import requests
import json
from AllCases.common.common import common

class debtPaymentInfo(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://192.168.9.128:8342/ebk-commission-api/commissionPayment/debtPaymentInfo'
        self.data = {
    "hotelId": "03201374",
    "operatorId": "15",
    "operatorName": "陶永红",
    "operateIp": "192.168.1.1",
    "debtPaymentInfoRequestList": [
        {
            "payTime": "2015-07-14 20:08:03",
            "payName": "五月账期",
            "payAmount": 24.2,
            "remark": "五月账单已付",
            "debtPaymentDetailRequestList": [
                {
                    "yearMonth": "2015-07-14 20:08:03",
                    "commisAmount": 12.1
                },
                {
                    "yearMonth": "2015-07-14 20:08:03",
                    "commisAmount": 12.1
                }
            ]
        },
        {
            "payTime": "2015-07-14 20:08:03",
            "payName": "五月账期",
            "payAmount": 24.2,
            "remark": "五月账单已付",
            "debtPaymentDetailRequestList": [
                {
                    "yearMonth": "2015-07-14 20:08:03",
                    "commisAmount": 12.1
                },
                {
                    "yearMonth": "2015-07-14 20:08:03",
                    "commisAmount": 12.1
                }
            ]
        }
    ]
}
        self.jData = json.dumps(self.data)
        self.loginHeader = {'content-type':'application/json'} 
        
    def tearDown(self):
        pass
    
    def testDebtPaymentInfo(self):
        tempCommon = common()
        self.req = requests.post(self.URL,data = self.jData, headers = self.loginHeader,cookies = tempCommon.getAssembleKeyInCookieInPortal())
        print "Get response:~~~~  ", self.req.content
        self.assertEquals(self.req.status_code, 200, 'return is not 200')
        
if __name__ == '__main__':
    unittest.main