import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG=27
ECHO=26
lcd_rs        = 25  # All are GPIO pins
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define no of Rows  and Columns
lcd_columns   = 16
lcd_rows      = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(2,GPIO.OUT)
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
            
            lcd.clear()
            lcd.show_cursor(True)
            lcd.message('Distance:%s'%(distance))
            print("Distance:",distance,"cm")
            if distance<10.00:
                  GPIO.output(2,1)
                  time.sleep(.3)
                  print("Intruder Detected !!!")
                  lcd.message('\nIntruder Detectd')
                  GPIO.output(2,0)
                  time.sleep(.3)
            time.sleep(1)
                        
except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit(0)       

                  
