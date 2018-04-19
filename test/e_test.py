# coding: utf-8

import socket
import select
import sys
from enum import Enum, unique
from future import Future

@unique
class EventType(Enum):
    input = 1
    socket = 2


class EventLoop(object):
    def __init__(self):
        self.events_to_listen = []
        self.callbacks = {}
        self.timeout = None

    def register_event(self, event, callback):
        self.events_to_listen.append(event)
        self.callbacks[event] = callback

    def unregister_event(self, event):
        self.events_to_listen.remove(event)
        del self.callbacks[event]

    def _process_events(self, events):
        for event in events:
            self.callbacks[event](self, event)

    def start_loop(self):
        while True:
            pass
            # 调用 select 函数，阻塞等待
            events = self.events_to_listen
            readable, writeable, exceptional = select.select(events, [], [])
            if len(readable) > 0:
                self._process_events(readable)


def stdin_callback(loop, event):
    junk = event.readline()
    print('junk', junk)


def data_callback(loop, event):
    sock = event
    data = sock.recv(1024)
    print('data', data)
    loop.unregister_event(sock)
    event.close()


def socket_callback(loop, event):
    server = event
    conn, addr = server.accept()
    # select 监听的socket
    loop.register_event(conn, data_callback)


def open_socket(port):
    host = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    s.bind((host, port))
    s.listen(5)
    print('listen {}:{}'.format(host, port))
    return s


def test():
    fd = sys.stdin
    socket_fd = open_socket(3000)

    loop = EventLoop()
    loop.register_event(fd, stdin_callback)
    loop.register_event(socket_fd, socket_callback)

    loop.start_loop()


def main():
    pass

if __name__ == '__main__':
    main()
