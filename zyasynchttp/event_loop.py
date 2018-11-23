# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/24 
@desc:
"""
from .selector import selector
from .task import Task


class EventLoop:
    stopped = False
    select_timeout = 5

    def __init__(self):
        self.selector = selector

    def run_until_complete(self, coros):
        tasks = [Task(coro) for coro in coros]
        try:
            self.run_forever()
        except StopIteration:
            self.close()
            pass

    def close(self):
        self.stopped = True

    def run_forever(self):
        selector = self.selector
        while not self.stopped:
            # 阻塞，直到一个事件发生
            events = selector.select()
            for event_key, event_mask in events:
                callback = event_key.data
                callback()
