from espeak import espeak
from time import sleep
count = 0
while True:
    espeak.synth('hello world')
    sleep(2)
    mystring = "current count is " + str(count)
    espeak.synth(mystring)
    sleep(2)
    count+=1
