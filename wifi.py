import Image
from pygooglechart import QRChart

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


	def createChart(self, width = 500, height = 500, encoding = 'H', padding = 2):
		self.chart = QRChart(width, height)
		self.chart.add_data(self.__str__())
		self.chart.set_ec(encoding, padding)
		
	def save(self, name = ''):
		if name == '':
			self.filename = self.ssid + '.png'
		else:
			self.filename = name
		self.chart.download(self.filename) #TODO: needs a test that chart exists
		print "Setup QR-Code saved as %s" %(self.filename)
	
	def display(self):
		self.save() # same here.
		Image.open(self.filename).show()
		
	def prettify(self):
		s = '''Your Settings are: 
SSID:           %s
Password:       %s
Authentication: %s
''' %(self.ssid, self.password, self.auth)
		return s
	
