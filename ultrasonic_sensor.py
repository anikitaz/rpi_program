from espeak import espeak
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
GPIO.setwarnings(False)
trig=14
echo=15
distance = 0
espeak.synth('welcome to audible ultrasonic distance meter')
print 'welcome to audible ultrasonic distance meter'
while True:
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.output(trig,False)
    sleep(2)
    print 'waiting..'
    espeak.synth('wait for calculations')
    GPIO.output(trig,True)
    time.sleep(0.0001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==False:
        start=time.time()
    time.sleep(0.00000005)
    while GPIO.input(echo)==True:
        finish=time.time()
    duration=finish - start
    dist=duration * 17150
    dist=round(dist,2)
    if( dist < 200 and dist > 0):
        distance = dist
    print 'distance is',distance,'cm'
    inputvalue=GPIO.input(26)
    if(inputvalue==True):
        sleep(1.5)
        mystring = "distance measured by ultrasonic sensor is " + str(distance)
        espeak.synth(mystring)
    sleep(5)
    
