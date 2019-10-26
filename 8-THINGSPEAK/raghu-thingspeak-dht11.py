import os
import time
import serial
import urllib2
import Adafruit_DHT
while 1 :
    try:
##        humidity,temperature = Adafruit_DHT.read_retry(11, 25) # Sensor,GPIO Pin
##        print ("Humidity =  %f" % humidity)
##        print("Temparature = %f" % temperature)
##        #print('Temp:{0:0.1f} C, Humidity:{1:0.1f} %'.format(temperature, humidity))
##        print ("------------------------------")
        humidity= 123
        temperature=576

        baseURL = "https://api.thingspeak.com/update?api_key=J3A5Q5TLP0PYC8F"
        g = urllib2.urlopen(baseURL + "&field1=%f, &field2=%f" % (humidity,temperature))
        print ("------------------------------")
        time.sleep(1)
    except:
        pass
    
