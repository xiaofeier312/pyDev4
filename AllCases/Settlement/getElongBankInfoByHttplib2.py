#encoding:utf-8
'''
Created on 2015��7��20��

@author: Zhijun.Zhou
'''
import unittest
import requests
import json

class getElongBankInfoByHttplib2(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testGetElongBankInfo(self):
        self.url = 'http://commission.ebooking.elong.com:8341/commission/commissionInfo/queryCommissionInfo'
        self.data = {"hotelId":"52407003"}
        self.jdata = json.dumps(self.data)
        self.header = {'content-type':'application/json'}
        self.myRequest = requests.post(self.url,data = self.jdata,headers = self.header)
        
        print 'return is:',self.myRequest.text
        print 'encoding is:',self.myRequest.encoding
        print 'json is:',self.myRequest.json
        print 'raw is',self.myRequest.raw
        print 'status code:',self.myRequest.status_code
        print 'request:',self.myRequest.request
        
if __name__ == '__main__':
    unittest.main
    