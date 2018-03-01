import RPi.GPIO as GPIO
import sleep as time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
while True:
    GPIO.output(27,GPIO.HIGH)
    sleep(1)
    GPIO.output(24,GPIO.LOW)
    sleep(1)
    GPIO.output(18,GPIO.HIGH)
    sleep(1)
    GPIO.output(18,GPIO.LOW)
    sleep(1)
    GPIO.output(24,GPIO.HIGH)
    sleep(1)
    GPIO.output(27,GPIO.LOW)
    sleep(1)
    
    
