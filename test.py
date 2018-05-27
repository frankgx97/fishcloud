from gpiozero import LED
from time import sleep

led = LED(2)

while True:
    led.toggle()
    sleep(1)