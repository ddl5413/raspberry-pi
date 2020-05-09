import RPi.GPIO as GPIO
import time


def roll(v, rt, st):
    GPIO.output(7, v[0])
    GPIO.output(11, v[1])
    time.sleep(rt)
    GPIO.output(7, 0)
    GPIO.output(11, 0)
    time.sleep(st)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    v = [0, 1]
    for i in range(0, 4):
        roll(v, 4, 2)
        v.reverse()
    GPIO.cleanup()


if __name__ == '__main__':
    main()



