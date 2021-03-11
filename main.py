from tornado.web import Application, RequestHandler, url
import tornado.ioloop


class Boilerplate(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', "*")

class HomeHandler(Boilerplate):
    def get(self):
        self.write('')

class CreateGameHandler(Boilerplate):
    def get(self): 
        pass

class JoinGameHandler(Boilerplate):
    def get(self):
        pass

class LeaveGameHandler(Boilerplate):
    def get(self):
        pass


def init():
    return Application([
        url(r'/', HomeHandler),
        url(r'/creategame', CreateGameHandler),
        url(r'/joingame', JoinGameHandler)
    ])

app = init()
app.listen(8000)
tornado.ioloop.IOLoop.current().start()