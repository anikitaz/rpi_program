import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
count=0
while True:
    inputvalue=GPIO.input(26)
    if(inputvalue==True):
        count=count+1
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        print("count"+str(count)+"times")
    time.sleep(0.1)
