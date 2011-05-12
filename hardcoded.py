from wifi import Wifi

w = Wifi(password = 'mysecret', auth='WPA', ssid='mySSID')
w.createChart(size=4)
w.display()