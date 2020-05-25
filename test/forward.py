import RPi.GPIO as GPIO
import time


def forward():
    GPIO.output(35, 1)
    GPIO.output(37, 0)
    time.sleep(20)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    forward()
    GPIO.cleanup()


if __name__ == '__main__':
    main()



