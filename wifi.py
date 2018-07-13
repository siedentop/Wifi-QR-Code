#Copyright: 2011 Christoph Siedentop
#License: This code is licensed under the GPLv3. For more see LICENSE

from pyqrnative.PyQRNative import QRCode, QRErrorCorrectLevel

class Wifi():
	def __init__(self, ssid = '', password = '', auth = 'WPA'):
		assert(isinstance(ssid, str))
		assert(isinstance(auth, str))
		assert(isinstance(password, str))
		self.ssid = ssid
		self.auth = auth
		self.password = password
		
	def __str__(self):
		''' String-ify the wifi configuration according to the definition found here: 
http://code.google.com/p/zxing/wiki/BarcodeContents#Wifi_Network_config_(Android)
The result is like this: WIFI:T:WPA;S:mynetwork;P:mypass;; 

Parameter 	Example 	Description
T 	WPA 	Authentication type; can be WEP or WPA
S 	mynetwork 	Network SSID
P 	mypass 	Password 
'''
		return "WIFI:T:" + self.auth + ";S:" + self.ssid + ";P:" + self.password + ";;"


	def createChart(self, size=10, level = QRErrorCorrectLevel.M):
		self.qr = QRCode(size, level)
		self.qr.addData(self.__str__())
		self.qr.make()
		self.image = self.qr.makeImage()
		
	def save(self, name = ''):
		if name == '':
			self.filename = self.ssid + '.png'
		else:
			self.filename = name
		self.image.save(self.filename, 'PNG')
		print("Setup QR-Code saved as %s" %(self.filename))
	
	def display(self):
		self.image.show()
		
	def prettify(self):
		s = '''Your Settings are: 
SSID:           %s
Password:       %s
Authentication: %s
''' %(self.ssid, self.password, self.auth)
		return s
	
