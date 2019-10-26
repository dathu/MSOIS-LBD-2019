#import os # to execte relay script
import RPi.GPIO as GPIO #to use GPIO pins for Sensor and actuators


import Adafruit_DHT #to featch temp and humidity
GPIO.setmode(GPIO.BCM)  # to initialise GPIO board
GPIO.setwarnings(False)


while 1 :
    try:
        
        humidity, temperature = Adafruit_DHT.read_retry(11, 4) #featches temp and humidity
        print ("------------------------------")
        print ("Relative Humidity =  %d" % humidity)
        print("Temparature Degree Celcius = %d" % temperature)
        print ("------------------------------")

        time.sleep(2)
    except:
        pass
    
