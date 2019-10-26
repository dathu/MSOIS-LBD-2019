import time
import Adafruit_DHT

from RPLCD import CharLCD

#import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23]) # physical board layout numbers

# Print a two line message
lcd.clear()
lcd.write_string('Hello world!')
time.sleep(1.0)

while(1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # Sensor, GPIO Pin
    print('Temp:{0:0.1f} C\n Humidity:{1:0.1f} %'.format(temperature, humidity))
    lcd.clear()
    lcd.cursor_pos=(0,0)
    lcd.write_string('Temp:%d'%(temperature))
    lcd.cursor_pos=(1,0)
    lcd.write_string('Humidity:%d'%(humidity))
    #lcd.write_string('Temp:{0:0.1f} Humidity:{1:0.1f} %'.format(temperature, humidity))
    time.sleep(2.0)
    
 
    
