from gpiozero import Servo
from time import sleep

servo = Servo(21)
servo.max()

def feed_fish():
  servo.min()
  sleep(2)
  servo.max()
  return servo.value

if __name__ == '__main__': 
  while True:
    print feed_fish()