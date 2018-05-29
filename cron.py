#coding:utf8
import requests
import platform

'''本脚本应添加到cron，用于监测水温。'''
if platform.system() == 'Darwin':
    print "Running on Darwin"
    import temperature_test as temperature
    import light_test as light
else:
    print "Running on other Platform"
    import temperature as temperature
    import light as light

def tempMonitor():
    rst = temperature.temp_range()
    if rst[0] != 'Normal':
        print rst[0]
        alarm(rst[1],rst[0])
        return True
    else:
        print 'Normal'
        return False

def alarm(v1,v2):
    requests.post(
        'https://maker.ifttt.com/trigger/fishcloud_water_alarm/with/key/cfY4fGDsxx4OnH3h5Gy5tT',
        json={'value1':v1,'value2':v2}
        )

tempMonitor()