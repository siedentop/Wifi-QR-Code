#!/usr/bin/env python

#Copyright: 2011 Christoph Siedentop
#License: This code is licensed under the GPLv3. For more see LICENSE


from wifi import Wifi
from optparse import OptionParser

if __name__=="__main__":
	parser = OptionParser(description='Generate Wifi-Settings for a smartphone (Android, etc).')
	parser.add_option("-s", "--ssid", dest="ssid",
                  help='The SSID (network name) of your Wifi.', metavar="SSID")
	parser.add_option("-p", "--password", dest="password",
                  help='the password for your wifi')

	parser.add_option('-a', '--auth', dest='auth', help = 'The type of authentication used. Can be WEP or WPA (default WPA)', default='WPA')
	(options, args) = parser.parse_args()
	
	if len(args) == 0:
		try:
			w = Wifi(password=options.password, auth=options.auth, ssid=options.ssid)
			print w.prettify()
			w.createChart()
			w.display()
		except:
			parser.print_help()
	else:
		parser.print_help()
	