#encoding:utf-8
'''
Created on Jul 19, 2015

@author: light
'''
import lib.HTMLTestRunner
import unittest
import time

class common(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.casesList = [
                          'AllCases.HomePrice.ChangePrice',
                          'AllCases.HomePrice.getPrice1',
                          'AllCases.Settlement.getElongBankInfoByHttplib2'
                          ]
    
if __name__ == "__main__":
    testunit = unittest.TestSuite()
    
    #run all cases
    for testcase in common().casesList:
        print "running cases:", testcase
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromName(testcase))
    
    filename="../../Reports/Result-"+time.strftime("%Y-%m-%d-%Hh%Mm%Ss", time.localtime())+".html"  #�����������·����֧�����·����
    fp=file(filename,'wb')
    runner = lib.HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #ʹ��HTMLTestRunner���ò����������·����������⡢����
    runner.run(testunit)