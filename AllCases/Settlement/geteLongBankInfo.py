#encoding:utf-8
'''
Created on 2015��7��20��

@author: Zhijun.Zhou
'''

import unittest
import urllib2
import json
 

class Settlement(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testGetElongInfo(self):
        self.url = 'http://commission.ebooking.elong.com:8341/commission/commissionInfo/queryCommissionInfo'
        self.sendValues = {"hotelId":"52407003"}
        self.jdata = json.dumps(self.sendValues)
        self.req = urllib2.Request(self.url,self.jdata)
        print self.jdata,"--",self.__str__()
        #Test
        #self.req.add_header('Content-Type', 'application/json; charset=UTF-8')
        
        self.req.add_header('Accept', '*/*')
        self.req.add_header('Accept-Encoding','gzip,deflate')
        self.req.add_header('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6')
        self.req.add_header('Connection', 'keep-alive')
        self.req.add_header('Content-Type', 'application/json')
        self.req.add_header('X-Requested-With','XMLHttpRequest')
        #self.req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
        self.req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36')
        #self.response = urllib2.urlopen(self.req)
        
        try:
            self.response = urllib2.urlopen(self.req)
        except Exception, ex:
            print Exception ,"--:",ex           
        finally:
            pass
        
        return self.response.read()


if __name__ == "__main__":
    unittest.main()
    #resp = Settlement()
   # strBack = resp.testGetElongInfo()
   # print strBack