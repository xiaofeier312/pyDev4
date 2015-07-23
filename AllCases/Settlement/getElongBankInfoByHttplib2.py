#encoding:utf-8
'''
Created on 2015��7��20��

@author: Zhijun.Zhou
'''
import unittest
import requests
import json
from AllCases.common.common import common

class getElongBankInfoByHttplib2(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
      
    def testGetElongBankInfo(self):
        self.loginUrl = 'http://commission.ebooking.elong.com:8341/commission/commissionInfo/queryCommissionInfo'
        self.loginData = {"hotelId":"52407003"}
        self.jdata = json.dumps(self.loginData)
        #self.loginCookies = requests.cookies.create_cookie('NewEbSessionId', 'eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlO\r\nYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6\r\nIjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFs\r\nc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYi\r\nLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRy\r\ndWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xl\r\nSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFm\r\nZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUw\r\nODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIs\r\nMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2ln\r\nbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=\r\n')
        
        self.tempCookieStr = common().getCookieInPortal()
        self.cookieFulsh = dict(NewEbSessionId = self.tempCookieStr )
        #self.cookieTemp = dict(NewEbSessionId = 'eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlOYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6IjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFsc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYiLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRydWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xlSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFmZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUwODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIsMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2lnbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=')
        self.loginHeader = {'content-type':'application/json'}
        #self.cookies = 'NewEbSessionId="eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlO\r\nYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6\r\nIjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFs\r\nc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYi\r\nLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRy\r\ndWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xl\r\nSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFm\r\nZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUw\r\nODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIs\r\nMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2ln\r\nbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=\r\n"'
        #self.cookiesNew = {'NewEbSessionId':'eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlO\r\nYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6\r\nIjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFs\r\nc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYi\r\nLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRy\r\ndWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xl\r\nSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFm\r\nZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUw\r\nODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIs\r\nMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2ln\r\nbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=\r\n'}
        #self.loginHeaderNew = {'content-type':'application/json', 'cookie':'''NewEbSessionId="eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlO\r\nYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6\r\nIjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFs\r\nc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYi\r\nLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRy\r\ndWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xl\r\nSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFm\r\nZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUw\r\nODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIs\r\nMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2ln\r\nbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=\r\n"'''}
        self.myRequest = requests.post(self.loginUrl,data = self.jdata,headers = self.loginHeader,cookies=self.cookieFulsh)
        #self.loginCookies = requests.cookies.create_cookie('NewEbSessionId', 'eyJob3RlbCI6eyJhZGRpdGlvbmFsU3RhdHVzIjoiMTQ0IiwiY2l0eUlkIjoiMjQwNyIsImNpdHlO\r\nYW1lIjoi5LuB5oCA77yI6YG15LmJ77yJIiwiZ3Vlc3RSb29tQW1vdW50Ijo4MCwiaG90ZWxJZCI6\r\nIjEwMTAxMTI5IiwiaG90ZWxOYW1lIjoiQVBJ5rWL6K+V6YWS5bqXIiwiaXNEaXNhYmxlZCI6ZmFs\r\nc2UsInNob3RlbENvbnRhY3RvciI6IuW8oOS4iSIsInNob3RlbFBob25lIjoiMTMyMDYzNTQzOTYi\r\nLCJzdGFyIjoiNSJ9LCJob3RlbElkIjoiMTAxMDExMjkiLCJpZCI6MjUwODYsImlzTG9naW4iOnRy\r\ndWUsInNlc3Npb25JZCI6ImYxZjBhMGE2NWQ0NTQwODNhNTM1NTZhOGIzYWNiNTUwIiwic2luZ2xl\r\nSG90ZWxTaWduIjoiMSIsInN0YWZmTGV2ZWwiOjEsInN0YWZmTmFtZSI6InpoaWFwaWEiLCJzdGFm\r\nZk5hbWVFbiI6InpoaWFwaSIsInRpbWVTdGFtcCI6MTQzNzQ0NTA1NzQwMywidXNlcklkIjoiMjUw\r\nODYiLCJ1c2VyTmFtZSI6InpoaWFwaSIsInVzZXJSaWdodCI6IjEsMiw0LDUsNyw4LDksMTAsMTIs\r\nMTMsMTQsMjYsMjcsMzMsMzQsMzUsMzksNDAsNDEsNDMsNDUsNDYsNDciLCJ1c2VyU291cmNlU2ln\r\nbiI6IkVCIiwidXNlclR5cGUiOiIyIn0=\r\n')
        
        print 'return is:',self.myRequest.text
        dataDic = common().switchHttpStrToDic(self.myRequest.text)
        self.assertEquals(dataDic['retcode'], 0, 'retcode is not 0')
        print '~~~~~~~~~~~~~@@Case \'testGetElongBankInfo\' over~~~~~~~~~~~~'
    

    '''    
    def testCommissionBill(self):
        self.URLCommissionBill = 'http://commission.ebooking.elong.com:8341/commission/commissionBill/initQueryCommissionBill'
        self.loginDataCommissionBill = {"hotelId":"52407003"}
        self.loginHeader = {'content-type':'application/json'}        
        self.jloginDataCommissionBill = json.dumps(self.loginDataCommissionBill)
        
        tempCommon = comGetCases
        
        print 'comGetCasestempCookie',tempCommon.tempCookie
        
        self.myRequestCommisonBill = requests.post(self.URLCommissionBill,data = self.jloginDataCommissionBill,headers = self.loginHeader,cookies=tempCommon.getAssembleKeyInCookieInPortal())
        print 'type self.myRequestCommisonBill:',type(self.myRequestCommisonBill.status_code)
        self.assertEquals(self.myRequestCommisonBill.status_code, 200, 'status.code is not 200')
        #print 'gobal var', comGetCasestempCookie,time.strftime("%Y-%m-%d-%Hh%Mm%Ss", time.localtime())
        #print 'gobal var', comGetCasestempCookie,time.strftime("%Y-%m-%d-%Hh%Mm%Ss", time.localtime())
        print '~~~~~~~~~~~~~@@Case \'testCommissionBill\' over~~~~~~~~~~~~'
    '''
        
if __name__ == '__main__':
    unittest.main
    