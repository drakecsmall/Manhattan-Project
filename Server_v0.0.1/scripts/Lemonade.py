from defaults import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,True)
time.sleep(pour_time)
GPIO.output(12,False)
GPIO.cleanup()