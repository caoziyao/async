# coding: utf-8

import socket

class Client(object):

    def __init__(self):
        self.sock = self.open_socket(3000)
        self.resp = b''

    def open_socket(self, port):
        host = 'localhost'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setblocking(False)

        s.bind((host, port))
        s.listen(5)
        print('listen {}:{}'.format(host, port))
        return s

    def read(self):
        chunk = self.sock.recv(4096)
        print('chunk', chunk)

