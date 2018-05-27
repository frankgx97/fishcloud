import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    GPIO.output(channel, 1)
    time.sleep(1)
    GPIO.output(channel, 0)  
    time.sleep(1)  

GPIO.cleanup()  