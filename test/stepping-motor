import RPi.GPIO as GPIO
import time

def step(i1,i2,i3,i4):
	GPIO.output(7,i1)
	GPIO.output(11,i2)
	GPIO.output(13,i3)
	GPIO.output(15,i4)
	time.sleep(0.02)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
for i in range(0,1000):
	step(1,0,0,0)
	step(0,1,0,0)
	step(0,0,1,0)
	step(0,0,0,1)

