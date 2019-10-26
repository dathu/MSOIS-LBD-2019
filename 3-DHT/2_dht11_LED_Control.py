import time
import RPi.GPIO as GPIO
#import sys
import Adafruit_DHT
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
try:
    while(1):
        humidity, temperature = Adafruit_DHT.read_retry(11, 4) # Sensor,GPIO 4th Pin
        print('Temp:{0:0.1f} C, Humidity:{1:0.1f} %'.format(temperature, humidity))
        if temperature>25:
            GPIO.output(19,1)
            print("Over Heating !!!")
            time.sleep(1)
            GPIO.output(19,0)
            time.sleep(1)
except KeyboardInterrupt:
      GPIO.cleanup()
      sys.exit(0)
