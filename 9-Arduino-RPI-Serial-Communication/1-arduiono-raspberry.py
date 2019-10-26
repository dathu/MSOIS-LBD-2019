import os
import serial, time
ser = serial.Serial('/dev/ttyACM0', 9600)


while (1) :
    try:
        x = ser.readline()
        values = x.split()
        humidity = float(values[0].strip('\0'))
        temperature = float(values[1].strip('\0'))
        lightint = int(values[2].strip('\0'))  

        print ("Temperature=  %f" %temperature)
        print ("Humidity=  %f" %humidity)
        print ("Intensity= %d" %lightint)
        print ("------------------------------")
    

        time.sleep(0.01)
    except:
        pass
