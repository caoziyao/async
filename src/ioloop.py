# coding: utf-8
import selectors
import select
import sys

"""
核心的 I/O 循环
"""

class IOLoop(object):
    # epoll 监听事件的宏定义
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

    def remove_handler(self, event):
        self.unregister_event(event)

    # register
    def register_event(self, event, callback,  flag=None):
        if flag is None:
            self.events_to_listen.append(event)
            self.callbacks[event] = callback
        else:
            self.events_to_listen.append(event)
            self.callbacks[flag] = callback

    def unregister_event(self, event, flag=None):
        if flag is None:
            self.events_to_listen.remove(event)
            del self.callbacks[event]
        else:
            self.events_to_listen.remove(event)
            del self.callbacks[flag]

    def _process_events(self, events):
        for event in events:
            if event == sys.stdin:
                key = sys.stdin.readline()[0]
                if key == 'a':
                    print('a')
                    self.callbacks[key](event)
                elif key == 'b':
                    print('b')
                    self.callbacks[key](event)
                else:
                    print('key', key)
            else:
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
