import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Raspberry Pi pin configuration:
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

# Print a two line message
lcd.write_string('Hello world!')
time.sleep(1.0)
TRIG=11
ECHO=13
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#GPIO.setup(2,GPIO.OUT)
GPIO.output(TRIG,False)

try:
      while True:
            print("######################################")
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
            
            lcd.clear()
            #lcd.show_cursor(True)
            lcd.write_string('Distance:%s'%(distance))
            print("Distance:",distance,"cm")
            if distance<10.00:
                  #GPIO.output(2,1)
                  time.sleep(.3)
                  print("Intruder Detected !!!")
                  lcd.cursor_pos=(1,0)
                  lcd.write_string('Intruder Detectd')
                  #GPIO.output(2,0)
                  time.sleep(.3)
            time.sleep(1)
                        
except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit(0)       

                  
