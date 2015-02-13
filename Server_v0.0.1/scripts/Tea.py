from defaults import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,True)
time.sleep(pour_time)
GPIO.output(11,False)
GPIO.cleanup()