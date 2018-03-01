import RPi.GPIO as GPIO
import time
import datetime
count=0
GPIO.setmode(GPIO.BCM)
mylog = datetime.datetime.today()
mylog = datetime.datetime.now()
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    mylog = open('log.csv','w')
    mylog.write('Light,Hour,Minutes,Seconds,Date,Month,Year\n')
    while(GPIO.input(4)==False):
        count=count+1
    
    today = datetime.datetime.today()
    a = datetime.datetime.now()
    h = a.hour
    m = a.minute
    s = a.second
    d = a.day
    mn = a.month
    y = a.year
    mystring = str(count) + '-'+str(h) + ':'+str(a.minute) + ':'+str(a.second) + '-'+str(a.day) + ',' +str(a.month)+ ','+str(a.year) + '\n'
    print mystring
    mylog.write(mystring)
    time.sleep(1)
    mylog.flush()
    mylog.close()
    count=0
