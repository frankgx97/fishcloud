from gpiozero import Servo
from time import sleep

servo = Servo(21)

def feed_fish():
  servo.min()
  sleep(1)
  servo.max()
  sleep(1)

while True:
    feedfish()