# coding: utf-8
import selectors
import select
import sys


class EventLoop(object):
    # Constants from the epoll module
    _EPOLLIN = 0x001
    _EPOLLPRI = 0x002
    _EPOLLOUT = 0x004
    _EPOLLERR = 0x008
    _EPOLLHUP = 0x010
    _EPOLLRDHUP = 0x2000
    _EPOLLONESHOT = (1 << 30)
    _EPOLLET = (1 << 31)

    READ = _EPOLLIN

    def __init__(self):
        self.events_to_listen = []
        self.callbacks = {}
        self.timeout = None

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def start(self):
        self.start_loop()

    def add_handler(self, fd, handler, events):
        self.register_event(fd, handler)

    # register
    def register_event(self, event, callback):
        self.events_to_listen.append(event)
        self.callbacks[event] = callback

    def unregister_event(self, event):
        self.events_to_listen.remove(event)
        del self.callbacks[event]

    def _process_events(self, events):
        for event in events:
            self.callbacks[event](event)

    def start_loop(self):
        while True:
            pass
            # 调用 select 函数，阻塞等待
            events = self.events_to_listen
            readable, writeable, exceptional = select.select(events, [], [])
            if len(readable) > 0:
                self._process_events(readable)

    def close(self):
        pass
