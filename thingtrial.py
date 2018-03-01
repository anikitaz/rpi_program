#https://thingspeak.com/update?key=4TXF9R0ROTW7ITKT&field1=12&field2=43&field3=232
import RPi.GPIO as GPIO
import urllib2
import time
abc = 'https://thingspeak.com/update?key=4TXF9R0ROTW7ITKT'
GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    count=0
    while(GPIO.input(4)==False):
        count=count+1
    print count
    mylink=abc+'&field1='+str(count)
    print mylink
    response = urllib2.urlopen(mylink)
    print response.code
    time.sleep(15)
    count=0
