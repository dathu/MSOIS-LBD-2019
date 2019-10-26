import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG=27
ECHO=26

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

GPIO.output(TRIG,False)

try:
      while True:     
            print("Distance Measurement IN Progress")
            print("Waiting for Sensor To Settle")
            time.sleep(2)
            GPIO.output(TRIG,True)
            time.sleep(0.00001)
            GPIO.output(TRIG,False)
            while GPIO.input(ECHO)==0:
                  pulse_start= time.time()
            while GPIO.input(ECHO)==1:
                  pulse_end= time.time()
            pulse_duration=pulse_end-pulse_start
            distance= pulse_duration*17150
            distance= round(distance,2)
            print("Distance:",distance,"cm")
            
            if distance<10.00:
                  GPIO.output(18,1)
                  time.sleep(.3)
                  print("Intruder Detected !!!")
                  GPIO.output(18,0)
                  time.sleep(.3)
except KeyboardInterrupt:
      GPIO.cleanup()
      sys.exit(0)
