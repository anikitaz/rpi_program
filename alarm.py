import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import urllib2
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

print '                          Alarm System   \n'
while True:
    now=str(datetime.now())
    GPIO.output(18,GPIO.HIGH)
    sleep(1)
    GPIO.output(18,GPIO.LOW)
    sleep(1)
    print 'Sending email'
    fromaddr="Rpi.tests.readings@gmail.com"
    toaddr="patilnn22597@gmail.com"
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']="Mail from Rpi system."

    body="Message from alarm system \n"+str(now)+"\nAlarm Worked! \nThank you for using the system.]"

    msg.attach(MIMEText(body,'plain'))
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,"Rpireads0")
    text=msg.as_string()   
    server.sendmail(fromaddr,toaddr,text)
    print 'Email sent!\n'
    sleep(2)
