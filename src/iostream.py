# coding: utf-8

from src import ioloop

"""
对非阻塞式的 socket 的简单封装，以方便常用读写操作
处理套接字的 read/write。
"""

class IOStream(object):

    def __init__(self, sock, io_loop=None,):
        self.socket = sock
        self.socket.setblocking(False)
        self.io_loop = io_loop or ioloop.IOLoop.instance()

    def connect(self, address):
        """
        address: (host, port)
        """
        self.socket.connect(address)

    def read_until(self, delimiter, callback):
        data = self.read_bytes(1024)
        print('read_until', data)


    def read_bytes(self, num_bytes):
        sock = self.socket
        data = sock.recv(num_bytes)
        return data

    def write(self, data):
        sock = self.socket
        sock.send(data)

    def close(self):
        """close socket"""
        if self.socket is not None:
            self.io_loop.remove_handler(self.socket)
            self.socket.close()
            self.socket = None