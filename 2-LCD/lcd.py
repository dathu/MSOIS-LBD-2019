import Adafruit_CharLCD as LCD
import time

lcd_rs        = 26  # All are GPIO pins
lcd_en        = 19
lcd_d4        = 13
lcd_d5        = 6
lcd_d6        = 5
lcd_d7        = 11

# Define no of Rows  and Columns
lcd_columns   = 16
lcd_rows      = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)


while True:
    lcd.clear()
    lcd.show_cursor(True)
    lcd.message('Hello \nWorld')
    time.sleep(1)
