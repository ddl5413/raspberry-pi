import RPi.GPIO as GPIO
import time


def forward():
    GPIO.output(12, 1)
    GPIO.output(16, 0)
    time.sleep(20)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    forward()
    GPIO.cleanup()


if __name__ == '__main__':
    main()



