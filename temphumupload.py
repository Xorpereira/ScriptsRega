#!/usr/bin/python

import Adafruit_DHT
import requests
import time

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 12

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Fahrenheit convertion
temperature=temperature*9/5.0+32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
r=requests.get("http://rtupdate.wunderground.com/weatherstation/updateweatherstation.php?ID=IPAMPILH2&PASSWORD=u0dgvs0f&dateutc=now&humidity={1:0.1f}&tempf={0:0.1f}&realtime=1&rtfreq=10&action=updateraw".format(temperature, humidity))
	
#else:
#	print('Failed to get reading. Try again!')

