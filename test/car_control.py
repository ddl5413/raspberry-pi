import web
import time
import car

urls = ('/(.*)', 'Action')


class Action:
    signal = False
    count = 0

    def GET(self, action):
        if action == 'start':
            car.forward()
            Action.signal = True
            while Action.signal:
                Action.count += 1
                print(Action.count)
                time.sleep(1)
                if Action.count == 100:
                    break
        if action == 'stop':
            Action.signal = False


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


