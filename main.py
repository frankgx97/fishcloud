import time
import temperature

def temp_range():
  current_temp = temperature.read_temp()
  if current_temp > CRIT_TEMP_HIGH:
    state = 'Too high'
  elif current_temp < CRIT_TEMP_LOW:
    state = 'Too low'
  else:
    state = 'Normal'
  return state, current_temp

