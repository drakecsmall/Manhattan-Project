#Runs solenoids until they are primed

from defaults import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,True)
time.sleep(5)
GPIO.output(12,False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,True)
time.sleep(5)
GPIO.output(11,False)


GPIO.cleanup()