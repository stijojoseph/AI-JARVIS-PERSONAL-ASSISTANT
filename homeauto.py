import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

def fanl():
    GPIO.output(5,GPIO.LOW)
def fanh():
    GPIO.output(5,GPIO.HIGH)
def lightl():
    GPIO.output(3,GPIO.LOW)
def lighth():
    GPIO.output(3,GPIO.HIGH)
