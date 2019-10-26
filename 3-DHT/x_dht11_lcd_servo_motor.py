import RPi.GPIO as GPIO
import time
#import sys
import Adafruit_DHT

import Adafruit_CharLCD as LCD
                      
GPIO.setwarnings(False)          # do not show any warnings
GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers (like PIN29 as GPIO5)
GPIO.setup(3,GPIO.OUT)             # initialize GPIO3 as an output 
p = GPIO.PWM(3,50)              # GPIO3 as PWM output, with 50Hz frequency (Channel, Frequency)
p.start(2.5)                     # Set Servo initially to 0 degree 
#p.start(0)
#GPIO.setup(3,GPIO.OUT)

# Raspberry Pi pin configuration:
lcd_rs        = 25  # all Gpio numbers.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4
#pin_gpio      = 3

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2


# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
# Print a two line message
lcd.message('Hello\nworld!')
time.sleep(5.0)
lcd.clear()
while(1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 26)
    print ('Temp: {0:0.2f} C, Humidity: {1:0.1f} %'.format(temperature, humidity))
    lcd.message('Temp:{0:0.2f} C\nHumidity:{1:0.2f} %'.format(temperature, humidity))
    GPIO.output(3,False)
    if(temperature>28):
     p.ChangeDutyCycle(12.5)    # change duty cycle for getting the servo position to 180 degree
     time.sleep(1)              # sleep for 1 second
     p.ChangeDutyCycle(2.5)     # change duty cycle for getting the servo position to 0 degree
     time.sleep(1)              # sleep for 1 second
      
        
        
    

    


