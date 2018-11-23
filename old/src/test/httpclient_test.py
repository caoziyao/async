# coding: utf-8

from src.web import RequestHandler


class HelloWorldHandler(RequestHandler):

    def get(self):
        name = 'csy'
        self.set_header("Content-Type", "text/plain")
        r = self.finish("Hello {}!".format(name))
        return r

