import time
import temperature.py

CRIT_TEMP_LOW = 20
CRIT_TEMP_HIGH = 24
LISTEN_PERIOD = 1


def set_temp_range(low, high):
    CRIT_TEMP_LOW = low
    CRIT_TEMP_HIGH = high


def set_listen_period(timeperiod):
    LISTEN_PERIOD = timeperiod


def temp_range():
    current_temp = read_temp()
    if current_temp > CRIT_TEMP_HIGH:
        state = 'Too high'
    elif current_temp < CRIT_TEMP_LOW:
        state = 'Too low'
    else:
        state = 'Normal'
    return state, current_temp

while True:
    print(temp_range())
    time.sleep(LISTEN_PERIOD)

