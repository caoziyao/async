# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/23 
@desc:
遇到 io 事件(轮询/中断)，切换上下文(进程/线程/协程)
async 和 await， async 用于定义 coroutine，await 用于从 coroutine 返回。
"""
import time
from zyasynchttp.async_request import AsyncRequest
from zyasynchttp.event_loop import EventLoop

now = lambda: time.time()
import asyncio

@asyncio.coroutine

def main():
    start = now()

    request = AsyncRequest('www.baidu.com', '/', 80)
    r2 = AsyncRequest('www.qq.com', '/', 80)
    # task = Task(request.fetch())
    coros = [request.fetch(), r2.fetch()]

    loop = EventLoop()
    loop.run_until_complete(coros)

    print(now() - start)


if __name__ == '__main__':
    main()
