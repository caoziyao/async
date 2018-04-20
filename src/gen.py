# coding: utf-8

from src.future import Future
from collections import Generator
from src.task import Task

def _create_future():
    f = Future()
    return f


# @gen.coroutine 装饰的方法执行后返回 Future 对象
# 并且会将方法参数中的 “callback” 加入到 Future 完成后的回调列表中
def coroutine(func):
    """Decorator for asynchronous generators"""
    wrapped = func
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, Generator):
            Task(result)
            # r = next(result)
        # else:
        #     r = result
        # return r
    return wrapper