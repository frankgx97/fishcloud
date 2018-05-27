import RPi.GPIO as GPIO 
import time

RPi.GPIO.setmode(GPIO.BOARD)  
RPi.GPIO.setup(2, RPi.GPIO.OUT)  

while True
    GPIO.output(channel, 1)
    time.sleep(1)
    GPIO.output(channel, 0)
    time.sleep(1)

GPIO.cleanup()