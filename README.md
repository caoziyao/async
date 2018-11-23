

```
loop = EventLoop()
loop.register_event(fd, callback)
loop.start_loop()

```

todo
- httpserver
- timer
- input

上篇
了解 异步编程及其紧密相关的概念，如阻塞/非阻塞、同步/异步、并发/并行等
理解 异步编程是什么，以及异步编程的困难之处
理解 为什么需要异步编程
熟悉 如何从同步阻塞发展到异步非阻塞的
掌握epoll + Callback + Event loop是如何工作的
掌握 Python 是如何逐步从回调到生成器再到原生协程以支持异步编程的
掌握 asyncio 的工作原理

中篇
掌握 asyncio 标准库基本使用
掌握 asyncio 的事件循环
掌握 协程与任务如何使用与管理（如调度与取消调度）
掌握 同步原语的使用(Lock、Event、Condition、Queue)
掌握 asyncio 和多进程、多线程结合使用

下篇
理解 GIL 对异步编程的影响
理解 asyncio 踩坑经验
理解 回调、协程、绿程(Green-Thread)、线程对比总结
掌握 多进程、多线程、协程各自的适用场景
了解 Gevent/libev、uvloop/libuv 与asyncio的区别和联系
掌握 Python异步编程的一些指导细则