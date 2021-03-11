from tornado.web import Application, RequestHandler, url
import tornado.ioloop
import json
from string import ascii_letters
from random import choice

class Boilerplate(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', "*")

class HomeHandler(Boilerplate):
    def get(self):
        self.write('')

class CreateGameHandler(Boilerplate):
    def initialize(self):
        self.letters = list(ascii_letters)
    def create_new_key(self):
        key = ''
        for i in range(100):
            key += choice(self.letters)
        return key
    def get(self): 
        with open('opengames.json') as f:
            data = json.load(f)
        key = self.create_new_key()
        data.append(key)
    
        

class JoinGameHandler(Boilerplate):
    def get(self, key):
        pass

class LeaveGameHandler(Boilerplate):
    def get(self):
        pass


def init():
    return Application([
        url(r'/', HomeHandler),
        url(r'/creategame', CreateGameHandler),
        url(r'/joingame/(.+)', JoinGameHandler),
        url(r'/leavegame', LeaveGameHandler)
    ])

app = init()
app.listen(8000)
tornado.ioloop.IOLoop.current().start()