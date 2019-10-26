import time
#import sys
import Adafruit_DHT

while(1):
    humidity, temperature = Adafruit_DHT.read_retry(22, 4) # Sensor,GPIO Pin
    print("-------------------------------------------")
    print('Temp:{0:0.1f} C, Humidity:{1:0.1f} %'.format(temperature, humidity))
    print("-------------------------------------------")
