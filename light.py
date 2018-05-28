from gpiozero import LED
from time import sleep

led = LED(2)

def turn_on():
  led.on()
  return led.is_lit

def turn_off():
  led.off()
  return led.is_lit

def auto_control():
  ############not finished
  return 

#while True:
#  print(turn_on())
#  sleep(1)
#  print(turn_off())
#  sleep(1)