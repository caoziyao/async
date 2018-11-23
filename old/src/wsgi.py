# coding: utf-8

from src import web


class WSGIApplication(web.Application):

    def __init__(self, handlers=None, default_host="", **settings):
        web.Application.__init__(self, handlers)