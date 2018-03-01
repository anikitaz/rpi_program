import RPi.GPIO as GPIO
from flask import Flask
GPIO.setwarnings(False)
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():  
    return "Hello Nikita!!"

@app.route("/l1o")
def hello1():
    GPIO.output(24,GPIO.LOW)
    return "LED1 is ON!!"

@app.route("/l1f")
def hello2():
    GPIO.output(24,GPIO.HIGH)
    return "LED1 is OFF!!"

@app.route("/l23o")
def hello3():
    GPIO.output(25,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    return "LED 2&3 is ON!!"

@app.route("/l23f")
def hello4():
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    return "LED 2&3 is OFF!!"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
