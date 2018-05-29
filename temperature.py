import os
import glob
import time

CRIT_TEMP_LOW = 20
CRIT_TEMP_HIGH = 30
LISTEN_PERIOD = 1

def set_temp_range(low, high):
  CRIT_TEMP_LOW = low
  CRIT_TEMP_HIGH = high


def set_listen_period(timeperiod):
  LISTEN_PERIOD = timeperiod
  
  
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
  
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
  
def read_temp_raw(): #readfile to get temperature
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
  
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c #, temp_f

def temp_range():
  current_temp = read_temp()
  if current_temp > CRIT_TEMP_HIGH:
    state = 'Too high'
  elif current_temp < CRIT_TEMP_LOW:
    state = 'Too low'
  else:
    state = 'Normal'
  return state, current_temp
  
#while True:
#    print(read_temp())   
#    time.sleep(1)
