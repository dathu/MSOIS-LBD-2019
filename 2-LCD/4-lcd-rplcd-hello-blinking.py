import time
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

while True:
    lcd.write_string("Hello --> JNNCE!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)

#hit ctrl +z / c to exit program
