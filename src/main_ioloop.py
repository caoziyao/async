# coding: utf-8

import socket
import select
import sys
import time
from src.future import Future
from src.task import Task
from crawler import Crawler
from src.task import Task
from src.future import Future
from src.ioloop import IOLoop

# pyasync = PyAsync()
loop = IOLoop()
now = lambda: time.time()

def late():
    time.sleep(5)
    f = Future()
    return f


def coroutine(func):

    def wrap(*args, **kwargs):
        flag = False
        while True:
            f = Future()
            print('----start---------')
            def on_read2(event):
                print('on_read2')
                junk = event.readline()
                print('junk', junk)
                f.set_result(junk)

            if flag == False:
                flag = True
                loop.register_event(sys.stdin, on_read2)

            func(*args, **kwargs)
            print('fff')
            a = yield f
            print('after yided', a)

    return wrap

@coroutine
def hello():
    print('hello')


def test():

    Task(hello())
    loop.start_loop()
    loop.close()

def main():
    pass

if __name__ == '__main__':
    main()
