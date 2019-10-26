# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:43:34 2019

@author: dathe
"""

import time
import random
import urllib3 # Used for Python3

def read_from_sensor():
    temp = random.randint(25, 45)
    hum = random.randint(50, 60)
    return temp, hum

while(1):
    temp, hum = read_from_sensor()
    print("Temperature: ", temp, chr(176) + "C")
    print("Humidity: ", hum, "%rH")
    time.sleep(2.0)

    baseURL="https://api.thingspeak.com/update?api_key=V7FP6HYNAG3H3DFS"

    url= (baseURL + "&field1=%d,&field2=%d" % (temp, hum))

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print(response.status)
    print(response.data)
    print(response.headers)
    time.sleep(0.01)
