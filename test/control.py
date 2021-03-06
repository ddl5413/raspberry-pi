import RPi.GPIO as GPIO
import web
import time

urls = ('/action/(.*)', 'Action',
        '/html/control.html', 'HTML')

left = False
right = False
vectors = ((1, 0, 0, 0),
           (0, 1, 0, 0),
           (0, 0, 1, 0),
           (0, 0, 0, 1))
step = 0
turn_speed = 0.002


def turn_left():
    global left, right, step
    left, right = True, False
    while left:
        step += 1
        if step == 4:
            step = 0
        turn()
        time.sleep(turn_speed)


def stop_turn_left():
    global left
    left = False


def turn_right():
    global left, right, step
    left, right = False, True
    while right:
        step -= 1
        if step == -1:
            step = 3
        turn()
        time.sleep(turn_speed)


def stop_turn_right():
    global right
    right = False


def forward():
    GPIO.output(12, 1)
    GPIO.output(16, 0)
    GPIO.output(18, 1)
    print('forward')


def backward():
    GPIO.output(12, 0)
    GPIO.output(16, 1)
    GPIO.output(18, 1)
    print('backward')


def stop():
    GPIO.output(12, 0)
    GPIO.output(16, 0)
    GPIO.output(18, 0)
    print('stop')


def brake():
    GPIO.output(12, 0)
    GPIO.output(16, 0)
    GPIO.output(18, 1)
    print('brake')


def turn():
    global vectors, step
    GPIO.output(7, vectors[step][0])
    GPIO.output(11, vectors[step][1])
    GPIO.output(13, vectors[step][2])
    GPIO.output(15, vectors[step][3])


class Action:

    def __init__(self):
        print('init')
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        # forward engine control
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)

        # turn engine control
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

    def GET(self, action):
        print(f'action:{action}')
        if action == 'forward':
            forward()
        if action == 'backward':
            backward()
        if action == 'brake':
            brake()
        if action == 'stop':
            stop()
        if action == 'turn_left':
            turn_left()
        if action == 'stop_turn_left':
            stop_turn_left()
        if action == 'turn_right':
            turn_right()
        if action == 'stop_turn_right':
            stop_turn_right()

class HTML:

    def GET(self):
        return open('../html/control.html')


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
