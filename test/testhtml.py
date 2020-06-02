import web

urls = ('/html/control.html', 'HTML')


class HTML:

    def GET(self):
        return open('../html/control.html')


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()