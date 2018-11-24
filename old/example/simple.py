# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/23 
@desc:
http://python.jobbole.com/88291/
"""

import time
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stopped = False
urls_todo = ['/', '/1', '/2']

now = lambda: time.time()


# 异步调用执行完的时候，就把结果放在它里面
class Future(object):

    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        """
        result属性，用于存放未来的执行结果
        :param result:
        :return:
        """
        self.result = result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result


class Crawler(object):

    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        global stopped

        sock = socket.socket()
        yield from connect(sock, ('www.qq.com', 80))

        get = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format('www.qq.com')
        data = get.encode('ascii')
        sock.send(data)

        self.response = yield from read_all(sock)

        if urls_todo:
            urls_todo.remove(self.url)

        if not urls_todo:
            stopped = True


class Task(object):

    def __init__(self, coro):
        # coro就是fetch()生成器
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        """
        :param future:
        :return:
        """
        try:
            # send 会进入到 coro 执行， 即 fetch, 直到下次 yield
            # next_future 为 yield 返回的对象
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        # 给下一次的future添加step()回调。
        next_future.add_done_callback(self.step)


def connect(sock, address):
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


def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_readable)

    chunk = yield from f
    selector.unregister(sock.fileno())
    return chunk


def read_all(sock):
    response = []

    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)

    r = b''.join(response)
    print(r)


def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


if __name__ == '__main__':
    start = now()

    for url in urls_todo:
        crawler = Crawler(url)
        Task(crawler.fetch())
    loop()

    print(now() - start)
