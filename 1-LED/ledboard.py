import RPi.GPIO as GPIO  
import time

# blinking function

def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)

# set up GPIO17 output channel
GPIO.setup(11,GPIO.OUT)  
GPIO.setwarnings(False)

# blink GPIO17 10 times
for i in range(0,10):  
        blink(11)  
GPIO.cleanup()   
