#encoding:utf-8
'''
Created on 2015��7��21��

@author: Zhijun.Zhou
'''

import requests
import json
import re

class common(object):
    '''
    classdocs
    '''
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.tempCookie = 'wrong'#cookie ,all cases can use
        
        #Login 
        self.LoginName = 'zhiapi'
        self.passwd = 'aaaaaa1'
        self.loginUrl = 'http://ebooking.elong.com/EbookingNew/NewLogin.mvc/AjaxLogin'
        self.loginHeader = {'Referer': 'http://ebooking.elong.com/EbookingNew/NewLogin.mvc/Login','Content-Type': 'application/x-www-form-urlencoded'}
        self.loginData = 'hotel_user=zhiapi&password=aaaaaa1&valicode=btrg&requestType=ajax&portaluser='
        self.portalUrl = 'http://192.168.9.128:8331/ebk-authentication-api/login/login'
        
        #get page displayed, so i can get cookie
        self.getPageUrl = 'http://ebooking.elong.com/ebookingnew/NewLogin.mvc/Login'
        self.getHeader = ''
        self.postLoginData = {"dataSource":["EBK","MIS"],"password":"aaaaaa1","source":"PC","userName":"zhiapi"}
        self.jpostLoginData = json.dumps(self.postLoginData)
        self.portalHeader = {'Content-Type': 'application/json','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
        
    def getfirstCookie(self):
        r1 = requests.get(self.getPageUrl,headers=self.getHeader)
        print r1.headers
        print 'r1.cookies--'
        print r1.cookies
        print 'r1.content--'
        print r1.content
        
    def getCookies(self):
        r = requests.post(self.loginUrl,data=self.loginData,headers = self.loginHeader)
        print r.headers
        print '----------'
        print r.text
        
    def getCookieInPortal(self):
        '''get cookie from portal'''
        r = requests.post(self.portalUrl,data=self.jpostLoginData,headers=self.portalHeader)
        print r.headers
        print '----------'
        print '1111',r.text
        print type(r.text)
        print '----------'
        jr = json.dumps(r.text)
        jrt = json.loads(jr)
        #
        print 'jrt:',jrt
        print 'type of jrt-----',type(jrt)
        jrt = json.loads(jrt)
        #jrt = unicodedata.normalize('NFKD', jrt).encode('ascii','ignore')
        print 'jrt@@@@@@@@ ',type(jrt)
        #jrt = json.loads(jrt)
        jrtFinal  = jrt['cookieStr']
        #print 'jrtFinal--',jrtFinal
        jrtFinal2 = re.sub('\\r\\n','',jrtFinal)
        print 'jrtFinal2:',jrtFinal2
        print type(jrtFinal)
        print '2----------'

        return jrtFinal2
    
    def getAssembleKeyInCookieInPortal(self):
        '''get Assemble cookie from portal'''
        r = requests.post(self.portalUrl,data=self.jpostLoginData,headers=self.portalHeader)
        print r.headers
        print '----------'
        print '1111',r.text
        print type(r.text)
        print '----------'
        jr = json.dumps(r.text)
        jrt = json.loads(jr)
        #
        print 'jrt:',jrt
        print 'type of jrt-----',type(jrt)
        jrt = json.loads(jrt)
        #jrt = unicodedata.normalize('NFKD', jrt).encode('ascii','ignore')
        print 'jrt@@@@@@@@ ',type(jrt)
        #jrt = json.loads(jrt)
        jrtFinal  = jrt['cookieStr']
        #print 'jrtFinal--',jrtFinal
        jrtFinal2 = re.sub('\\r\\n','',jrtFinal)
        print 'jrtFinal2:',jrtFinal2
        print type(jrtFinal)
        print '2----------'   
                
        #assemble assemble session and session ID>NewEbSessionId to a globa cookie string        
        self.tempCookie = dict(NewEbSessionId =  jrtFinal2 )    
        print 'self.tempCookieAAAA', self.tempCookie
    
        return self.tempCookie   
    
    def switchHttpStrToDic(self,httpStr):
        '''changing http unicode/body/json to dic'''
        jdata = json.dumps(httpStr)
        jdataT = json.loads(jdata)
        #jdataF = unicodedata.normalize('NFKD', jdataT).encode('ascii','ignore')
        jascii = json.loads(jdataT)
        print jascii['retcode']

        return jascii

    
        
if __name__ == '__main__':
    conn = common()
    conn.getAssembleKeyInCookieInPortal()