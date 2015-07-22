#encoding:utf-8
'''
Created on 2015

@author: Zhijun.Zhou
'''
import MySQLdb

class connMysql:
    #def __init__(self,IPNumber='14.203',*database='bms_ebooking'):
    def __init__(self,host='14.203',user='root',passwd ='abc123',db = 'bms_ebooking'):
        '''default is connecting to 14.23, for example: if you want to connect to 192.168.67.13, you can input 67.13 only
        or 192.168.67.13
        '''
        if host == '14.203':
            print 'use default connecting str 14.203'
            self.sqlUrl = '192.168.14.203'            
        elif (host == '67.13') or (host == '192.168.67.13'):
            self.sqlUrl = '192.168.67.13'
            self.sqluser = 'bdg1213'
            self.sqlpswd = 'LOM896yui'
            self.sqldb = 'null'
        else:
            self.sqlUrl = host
         
        #self.coon = ''
        try:
            self.coon = MySQLdb.Connect(host=self.sqlUrl,user=user,passwd = passwd,db =db)
            print     user,passwd,db
            self.cursor = self.coon.cursor()
        #self.cursor.close()
        except Exception,ex:
            print ex
        
    def connTest(self):
        '''abandon'''
        conn = MySQLdb.connect(host='192.168.14.203',user='root',passwd ='abc123',db = 'bms_ebooking')
        cursor = conn.cursor()
        cursor.execute("select version();")
        res = cursor.fetchall()
        print type(res),res
        cursor.execute('show databases;') 
        res1 = cursor.fetchall()
        print type(res1),res1
        return [res,res1]
        cursor.close()

if __name__ == '__main__':
    a = connMysql('67.13')
    print a.sqlUrl
    
    '''
    a.cursor.execute('select version();')
    res = a.cursor.fetchall()
    #resDic = res
    print res
    a.cursor.close()
    '''