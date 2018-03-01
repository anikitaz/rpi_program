from Adafruit_IO import *
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
GPIO.setwarnings(False)
sensor = Adafruit_DHT.DHT11
pin = 17
aio = Client('b666134b9f664db58c3824478208d2a6')
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    count=0
    while(GPIO.input(4)==False):
        count=count+1
    print 'LDR count = ',count
    aio.send('ldr',count)
    count=0
    time.sleep(0.4)
        
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print 'Temperature = ',temperature
        print 'Humidity = ',humidity
    aio.send('temp',temperature)
    aio.send('hum',humidity)
    time.sleep(0.4)

    data1=aio.receive('sw1')
    if(data1.value=='ON'):
        GPIO.output(24,GPIO.LOW)
        print 'LED1 On'
        time.sleep(0.4)
    else:
        GPIO.output(24,GPIO.HIGH)
        print 'LED1 Off'
        time.sleep(0.4)

    data2=aio.receive('sw2')
    if(data2.value=='ON'):
        GPIO.output(8,GPIO.LOW)
        print 'LED2 On'
        time.sleep(0.4)
    else:
        GPIO.output(8,GPIO.HIGH)
        print 'LED2 Off'
        time.sleep(0.4)

    r=aio.receive('sw3')
    if (r.value=='ON'):
        GPIO.output(27,GPIO.HIGH)
        print 'Relay ON'
        time.sleep(0.4)
    else:
        GPIO.output(27,GPIO.LOW)
        print 'Relay Off'
        time.sleep(0.4)
    
