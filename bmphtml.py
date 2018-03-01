from flask import Flask,render_template
import datetime
import Adafruit_BMP.BMP085 as BMP085
from time import sleep
sensor = BMP085.BMP085()
app=Flask(__name__)
@app.route("/")
def hello():
    now= datetime.datetime.now()
    timeString=now.strftime("%Y-%m-%d %H:%M:%S")
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()
    altitude = round(altitude,2)
    sea_level = sensor.read_sealevel_pressure()
    templateData={
        'title':'BMP180!',
        'time':timeString,
        'temp':temperature,
        'pres':pressure,
        'alti':altitude,
        'sealevel':sea_level,
        }
    return render_template('main.html',**templateData)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
