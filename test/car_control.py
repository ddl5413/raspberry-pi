import RPi.GPIO as GPIO
import web
import time

urls = ('/(.*)', 'Action')


class Action:
    signal = False
    count = 0

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

    def GET(self, action):
        if action == 'start':
            Action.forward()
            Action.signal = True
            while Action.signal:
                Action.count += 1
                print(Action.count)
                time.sleep(1)
                if Action.count == 100:
                    break
        if action == 'stop':
            Action.signal = False
            Action.stop()

    def urn_left(self):
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


