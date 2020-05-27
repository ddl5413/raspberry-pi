import RPi.GPIO as GPIO
import web
import time

urls = ('/(.*)', 'Action')


class Action:

    def __init__(self):
        print('init')
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

    def GET(self, action):
        print(f'action:{action}')
        if action == 'start':
            Action.forward(self)
        if action == 'stop':
            Action.stop(self)

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


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


