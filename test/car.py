import RPi.GPIO as GPIO
import time


class Car:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        print('init')

    def turn_left(self):
        print('left')

    def turn_right(self):
        print('right')

    def forward(self):
        GPIO.output(12, 1)
        GPIO.output(16, 0)
        print('forward')


    def stop(self):
        GPIO.output(12, 0)
        GPIO.output(16, 0)
        print('stop')
