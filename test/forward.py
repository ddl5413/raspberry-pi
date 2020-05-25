import RPi.GPIO as GPIO
import time


def forward():
    GPIO.output(7, 1)
    GPIO.output(11, 0)
    time.sleep(20)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    forward()
    GPIO.cleanup()


if __name__ == '__main__':
    main()



