# coding: utf-8
import socket
import selectors
from selectors import EVENT_READ, EVENT_WRITE
from future import Future

sel = selectors.DefaultSelector()

class Crawler(object):

    def __init__(self, url):
        self.url = url
        self.response = b''


    def fetch(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)

        try:
            sock.connect(('localhost', 3000))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            f.set_result(None)

        sel.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield f
        sel.unregister(sock.fileno())

