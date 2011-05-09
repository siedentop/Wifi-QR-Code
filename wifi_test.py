import unittest
from wifi import Wifi

class TestWifi(unittest.TestCase):
	def setUp(self):
		pass

	def test_string(self):
		# Get the string out correctly
		''' String-ify the wifi configuration according to the definition found here: 
http://code.google.com/p/zxing/wiki/BarcodeContents#Wifi_Network_config_(Android)
The result is like this: WIFI:T:WPA;S:mynetwork;P:mypass;; 

Parameter 	Example 	Description
T 	WPA 	Authentication type; can be WEP or WPA
S 	mynetwork 	Network SSID
P 	mypass 	Password'''
		uut = Wifi(password = 'mypass', ssid = 'mynetwork', auth = 'WPA')
		self.assertEqual(uut.__str__(), 'WIFI:T:WPA;S:mynetwork;P:mypass;;')
		
	def test_constructor(self):
		'''Only strings can be input'''
		self.assertRaises(Wifi(password = 12, ssid = 'mynet'), '')
		

       


if __name__ == '__main__':
	unittest.main()
