from RPLCD import CharLCD
from RPLCD import CursorMode
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

lcd.write_string('HELLO JNNCE!')

#lcd.cursor_mode = CursorMode.blink
#lcd.cursor_mode = CursorMode.line
lcd.cursor_mode = CursorMode.hide
