import RPi.GPIO as GPIO
import time
def allonoff():
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(0.1)

def fonoff():
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(0.1)
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)
myflag = 0
while True:
    inputvalue=GPIO.input(26)
    if (inputvalue==True and (myflag == 0 or myflag == 20)):
        myflag = 10
        time.sleep(1)
            
    inputvalue=GPIO.input(26)
    if (inputvalue==True and myflag == 10):
        myflag = 20
        time.sleep(1)

    if myflag == 10:
        allonoff() 
    if myflag == 20:
        fonoff()
      
            
