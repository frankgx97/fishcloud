#coding:utf8
from flask import Flask, render_template, request
from flask import jsonify
import platform

if platform.system() == 'Darwin':
    print "Running on Darwin"
    import temperature_test as temperature
    import light_test as light
else:
    print "Running on other Platform"
    import temperature as temperature
    import light as light
    import tinyservo as tservo

app = Flask(__name__, static_url_path='/static')  # 定义/static目录为静态文件目录

@app.route("/")
def index():
    '''渲染首页HTML模板'''
    return render_template('index.html')

@app.route("/action/feed")
def feed():
    '''投喂'''
    return jsonify({
		tservo.feed_fish()
        "state":True
    })

@app.route("/action/lighton")
def lightOn():
    '''开灯'''
    return jsonify({
        'state':light.turn_on()
    }) 

@app.route("/action/lightoff")
def lightOff():
    '''关灯'''
    return jsonify({
        'state':light.turn_off()
    }) 

@app.route("/read/temp")
def getWaterTemp():
    '''读取水温'''
    return jsonify({
        'state':temperature.temp_range()[0],
        'temp':temperature.temp_range()[1]
    })

@app.route("/read/light")
def getLightStat():
    '''读取灯光状态'''
    return jsonify({
        'state':light.getStat()
    })
