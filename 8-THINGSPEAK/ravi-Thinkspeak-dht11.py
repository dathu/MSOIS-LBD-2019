import time
import Adafruit_DHT
#import os # to execte relay script
import RPi.GPIO as GPIO #to use GPIO pins for Sensor and actuators
import serial, time 
import urllib2 # to use thingspeak URL to see Graps

#import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Print a two line message
lcd.write_string('Hello world!')
time.sleep(1.0)

while(1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # Sensor,GPIO Pin
    print('Temp:{0:0.1f} C\n Humidity:{1:0.1f} %'.format(temperature, humidity))
    lcd.clear()
    lcd.cursor_pos=(0,0)
    lcd.write_string('Temp:%d'%(temperature))
    lcd.cursor_pos=(1,0)
    lcd.write_string('Humidity:%d'%(humidity))
    #lcd.write_string('Temp:{0:0.1f} Humidity:{1:0.1f} %'.format(temperature, humidity))
    time.sleep(2.0)


    baseURL = "https://api.thingspeak.com/update?api_key=XQZHR38E00B9GRDN"

    g = urllib2.urlopen(baseURL + "&field1=%d, &field2=%d" % (temperature,humidity))
    time.sleep(0.01)
    
    
