#encoding:utf-8
'''
Created on 2015年7月23日

@author: Zhijun.Zhou
'''
#import AllCases.GetCases.GetCases
import json
from AllCases.common.common import common
import requests
import unittest

class initCommissionBill(unittest.TestCase):
    def setUp(self):
        self.URLCommissionBill = 'http://commission.ebooking.elong.com:8341/commission/commissionBill/initQueryCommissionBill'
        self.loginDataCommissionBill = {"hotelId":"52407003"}
        self.loginHeader = {'content-type':'application/json'}        
        self.jloginDataCommissionBill = json.dumps(self.loginDataCommissionBill)

    def tearDown(self):
        pass
     
    def testCommissonBill(self):   
        tempCommon = common()
        
        #print 'GetCases().tempCookie',tempCommon.getAssembleKeyInCookieInPortal()        
        self.myRequestCommisonBill = requests.post(self.URLCommissionBill,data = self.jloginDataCommissionBill,headers = self.loginHeader,cookies=tempCommon.getAssembleKeyInCookieInPortal())
        print 'type self.myRequestCommisonBill:',type(self.myRequestCommisonBill.status_code)
        self.assertEquals(self.myRequestCommisonBill.status_code, 200, 'status.code is not 200')
        #self.assertEquals(self.myRequestCommisonBill.content())
        print '~~~~~~~~~~~~~@@Case \'testCommissionBill\' over~~~~~~~~~~~~'
        
     
    
if __name__ == '__main__':
    unittest.main