import unittest
import httplib
import json
import urllib
import urllib2

class MyTest(unittest.TestCase):
	def setUp(self):
		print "Case running..."

	def tearDown(self):
		print "Case end..."
		pass

	def test_home1(self):
		'''get home price'''
		#conn = httplib.HTTPConnection("192.168.14.94",8045)
		#path = "/bms-ebooking-api/sHotel/getSHotelDetailInfo"
		self.url="http://192.168.14.94:8045/bms-ebooking-api/sHotel/getSHotelDetailInfo"
		self.values = {"hotelId":"10101594","queryFieldList":[1,2]}
		self.jdata = json.dumps(self.values)
		#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		#req = conn.request("POST",path,jdata,headers)
		#response = conn.getresponse()
		self.req2 = urllib2.Request(self.url,self.jdata)
		self.req2.add_header('Content-Type', 'application/json; charset=UTF-8')
		self.req2.add_header('X-Requested-With','XMLHttpRequest')
		self.req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
		self.response2 = urllib2.urlopen(self.req2)
		#print response.reason
		#print response.read()
		#print response.getheaders()
		#print "22222222222222"
		#print response2.status
		#print response2.reason
		self.result2 = self.response2.read()
		print self.result2
		print "type(result2): " ,type(self.result2)
		self.jresult = json.dumps(self.result2,indent = 4)
		#print jresult2
		#print response2.getheaders()
		print self.jresult
		#print type(jresult)
		self.assertEqual(200, 200)
		print "case:"

if __name__ == "__main__":
	unittest.main()
	