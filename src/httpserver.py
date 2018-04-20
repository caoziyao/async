# coding: utf-8

import errno
import logging
import os
import socket
from src import ioloop
from src import iostream
from src.test.httpclient_test import HelloWorldHandler

"""
服务于 web 模块的一个非常简单的 HTTP 服务器的实现
"""

class HTTPServer(object):
    def __init__(self, application, io_loop=None, ):
        self._sockets = {}  # fd -> socket object
        self._started = False
        self.io_loop = io_loop
        self.application = application

    def listen(self, port, host=''):
        self.bind(port, host)
        num_processes = 1
        self.start(num_processes)

    def bind(self, port, host=None, family=socket.AF_UNSPEC):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 非阻塞
        s.setblocking(False)
        # set option reused
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        self._sockets[s] = s

        self.io_loop = ioloop.IOLoop.instance()
        self.io_loop.add_handler(s, self._handle_events,
                                 ioloop.IOLoop.READ)

    def start(self, num_processes=1):
        self._started = True

    def _handle_events(self, event):
        print('_handle_events')
        conn, addr = event.accept()
        stream = iostream.IOStream(conn, io_loop=self.io_loop)
        HTTPConnection(stream, addr, self.application, self.io_loop)


class HTTPConnection(object):
    """
    处理与 HTTP client 建立的连接，解析 HTTP Request 的 header 和 body。
    """

    def __init__(self, stream, address, application, io_loop=None):
        self.stream = stream
        self.application = application
        self.io_loop = io_loop or ioloop.IOLoop.instance()
        self.io_loop.add_handler(stream.socket, self.request_callback, ioloop.IOLoop.READ)

    def request_callback(self, event):
        data = self.stream.read_bytes(1024)
        if data:

            data = data.decode()
            path = data.split(' ')[1]
            print('path', path)
            named_route = self.application.named_router
            handler = named_route.get(path, None)
            if handler is not None:
                r = handler(self.application).get(self.stream)
            #     # print('raaa', r)
            #     # self.stream.write(r)
            else:
                self.stream.close()
        else:
            self.stream.close()
