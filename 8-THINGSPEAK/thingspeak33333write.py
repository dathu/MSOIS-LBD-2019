# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:49:04 2019

@author: dathe
"""

import time
import random
#import os # to execte relay script
#import RPi.GPIO as GPIO #to use GPIO pins for Sensor and actuators
#import urllib2 # to use thingspeak URL to see Graps

import urllib.request #USed for python 3

def read_from_sensor():
    temp = random.randint(25,45)
    hum = random.randint(50,60)
    air = random.randint(55,60)
    light = random.randint(100,180)
    return temp, hum, air,light

while(1):
    temp,hum,air,light = read_from_sensor()
    print("Temperature:",temp, chr(176) + "C")
    print("Humidity:", hum,"%rH") 

    time.sleep(2.0)


    baseURL = "https://api.thingspeak.com/update?api_key=V7FP6HYNAG3H3DFS"

    g = urllib.request.urlopen(baseURL + "&field1=%d, &field2=%d" % (temp,hum))
    
    time.sleep(0.01)
