from gpiozero import LED, TimeOfDay
from time import sleep
from datetime import time
from signal import pause

led = LED(2)

def set_time(sh,sm,ss,eh,em,es):
  duringtime = TimeOfDay(time(sh,sm,ss), time(eh,em,es))
  led.source = duringtime.values
  return duringtime# led.is_lit

def turn_on():
  led.on()
  return led.is_lit

def turn_off():
  led.off()
  return led.is_lit

def auto_control():
  ############not finished
  return 

print set_time(7,49,0,23,0,0)
pause()
#while True:
#  print(turn_on())
#  sleep(1)
#  print(turn_off())
#  sleep(1)