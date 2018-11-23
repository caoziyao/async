# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/24 
@desc:
"""
from .future import Future

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