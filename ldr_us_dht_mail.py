import smtplib
import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_DHT
import urllib2
abc = 'https://thingspeak.com/update?key=TLX6QROSEXZQUGXR'
count=0
sensor = Adafruit_DHT.DHT11
pin = 17
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("Rpi.tests.readings@gmail.com","Rpireads0")
GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while(GPIO.input(4)==False):
        count=count+1
    mystring = str(count) 
    print mystring
    count=0

    
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print humidity
        print temperature
    time.sleep(2)
    
    mylink=abc+'&field1='+str(count)+'&field2='+str(humidity)+'&field3='+str(temperature)+'\n'
    print mylink
    response = urllib2.urlopen(mylink)
    print 'Sending email'
    
    mymsg = "Hi\nLDR is "+str(count)+"\nHumidity is "+str(humidity)+"\nTemperature is "+str(temperature)
    server.sendmail("Rpi.tests.readings","patilnn22597@gmail.com",mymsg)
    print response.code
    print 'Email sent!\n'
    time.sleep(5)
    
