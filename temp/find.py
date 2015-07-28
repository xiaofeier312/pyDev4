# -*- coding: utf-8 -*-
'''
Created on 2015��7��23
@author: Zhijun.Zhou
'''
import json
import sys
from encodings import ascii


a = '你好'
b = ['你好'.decode('utf-8'),1]
data = {
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
data1 = json.dumps(data)
print a
print b
print data
print data1
print sys.getdefaultencoding()
print sys.getfilesystemencoding()


if __name__ == '__main__':
    pass