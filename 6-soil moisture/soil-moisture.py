#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    x = GPIO.input(channel)
    print(x)
    if (x==0):
        print("------------------------------------")
        print("Soil is Wet (0)")
        print("Waiting for Sensor To Settle")
        time.sleep(2)
    else:
        print("------------------------------------")
        print("Soil is Dry (1)")
        print("Waiting for Sensor To Settle")
        time.sleep(2)
