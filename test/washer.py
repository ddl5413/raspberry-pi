import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

for i in range(0, 4):
    GPIO.output(7, 1)
    GPIO.output(11, 0)
    time.sleep(10)

    GPIO.output(7, 0)
    GPIO.output(11, 0)
    time.sleep(4)

    GPIO.output(7, 0)
    GPIO.output(11, 1)
    time.sleep(10)

    GPIO.output(7, 0)
    GPIO.output(11, 0)
    time.sleep(4)
GPIO.cleanup()
