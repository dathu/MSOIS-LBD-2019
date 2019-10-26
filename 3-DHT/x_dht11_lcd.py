import time
#import sys
import Adafruit_DHT

import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note All Pins are GPIO
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4
#

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2



# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


# Print a two line message
lcd.message('Hello\nworld!')
time.sleep(1.0)

while(1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 26) # Sensor,GPIO Pin
    print('Temp:{0:0.1f} C\nHumidity:{1:0.1f} %'.format(temperature, humidity))
    lcd.clear()
    lcd.message('Temp:{0:0.1f} C\nHumidity:{1:0.1f} %'.format(temperature, humidity))
    time.sleep(2.0)
    
