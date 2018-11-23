# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/24 
@desc:
"""
import time
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from .future import Future
from .task import Task
from .selector import selector


class AsyncRequest(object):

    def __init__(self, host, url, port, timeout=5):
        self.sock = socket.socket()
        # self.sock.settimeout(timeout)
        self.sock.setblocking(False)
        self.host = host
        self.url = url
        self.port = port
        self.method = None
        self.address = (host, port)
        self.selector = selector
        self.stopped = False

    def get(self):
        sock = self.sock

        self.method = 'GET'
        self.request = '{} {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.method, self.url, self.host)
        self.request = self.request.encode('ascii')
        sock.send(self.request)

    def connect(self):
        """

        :return:
        """
        sock = self.sock
        address = self.address
        selector = self.selector

        f = Future()
        sock.setblocking(False)

        try:
            # nonblocking
            sock.connect(address)
        except BlockingIOError as e:
            # 非阻塞连接过程中也会抛出异常
            # Operation now in progress”，这表示连接已经在建立但还没有完成
            print('connect', e)

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield from f

        selector.unregister(sock.fileno())

    def read(self):
        """

        :return:
        """
        sock = self.sock
        selector = self.selector
        f = Future()

        def on_readable():
            f.set_result(sock.recv(4096))

        selector.register(sock.fileno(), EVENT_READ, on_readable)

        chunk = yield from f
        selector.unregister(sock.fileno())
        return chunk

    def read_all(self):
        """

        :return:
        """
        sock = self.sock
        response = []

        chunk = yield from self.read()
        while chunk:
            response.append(chunk)
            chunk = yield from self.read()

        r = b''.join(response)
        print(r)

    def fetch(self):
        sock = self.sock

        yield from self.connect()

        self.get()

        self.response = yield from self.read_all()

        self.stopped = True
        return self.response
