import RPi.GPIO as GPIO
import time
led=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
while True:
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(24,GPIO.LOW)
    time.sleep(1)
    
