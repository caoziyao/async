# coding: utf-8

import errno
import logging
import os
import socket
import ioloop

class HTTPServer(object):

    def __init__(self, application, io_loop=None,):
        self._sockets = {}  # fd -> socket object
        self._started = False
        self.io_loop = io_loop


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

        self.io_loop = ioloop.EventLoop.instance()
        self.io_loop.add_handler(s, self._handle_events,
                                 ioloop.EventLoop.READ)

    def start(self, num_processes=1):
        self._started = True

    def _handle_conn(self, event):
        sock = event
        data = sock.recv(1024)
        print('data', data)
        if data:
            r = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World aas</h1>'
            sock.send(r)
            self.io_loop.unregister_event(sock)
            sock.close()
        else:
            # 移除select监听的socket
            self.io_loop.unregister_event(sock)
            sock.close()

    def _handle_events(self, event):
        print('_handle_events')
        s = self._sockets[event]
        if s == event:
            print('s == event')
            conn, addr = event.accept()
            self.io_loop.add_handler(conn, self._handle_conn, ioloop.EventLoop.READ)
        else:
            pass
