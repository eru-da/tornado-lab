import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<title>Dummy Page</title>')