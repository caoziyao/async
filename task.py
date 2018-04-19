# coding: utf-8

import time
from future import Future

class Task(object):
    def __init__(self, coro):
        self.coro = coro
        print('coro', coro)
        f = Future()
        f.set_result(None)
        self.step(f)


    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
            print('next_future')
        except StopIteration:
            return
        next_future.add_done_callback(self.step)