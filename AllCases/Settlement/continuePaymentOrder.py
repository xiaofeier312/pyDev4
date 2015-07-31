#encoding:utf-8
'''
Created on 2015年7月28日

@author: Zhijun.Zhou
'''
import unittest
import re
import json
import requests
from AllCases.common.common import common
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class continuePaymentOrder(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://192.168.9.128:8342/ebk-commission-api/commissionPayment/continuePaymentOrder'
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
    
    def testContnuePaymentOrder(self):
        tempCommon = common()
        self.req = requests.post(self.URL,data = self.jdata, headers = self.loginHeader, cookies = tempCommon.getAssembleKeyInCookieInPortal())
        print self.req.status_code
        print "Get response:~~~~ ", self.req.content
        self.assertEquals(self.req.status_code, 200, 'return is not 200')
        self.assertNotEqual(re.search('"retcode":0',self.req.content), None, "retcod is not 0")
        
if __name__ == '__main__':
    unittest.main
        
