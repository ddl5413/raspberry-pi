import RPi.GPIO as GPIO
import time


def roll(v, rt, st):
    if v == 1:
        GPIO.output(7, 1)
        GPIO.output(11, 0)
    else:
        GPIO.output(7, 0)
        GPIO.output(11, 1)
    time.sleep(rt)
    GPIO.output(7, 0)
    GPIO.output(11, 0)
    time.sleep(st)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)

    for i in range(0, 4):
        roll(i % 2, 4, 2)
    GPIO.cleanup()


if __name__ == '__main__':
    main()



