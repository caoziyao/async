# # coding: utf-8
#
# import time
# import sys
# import selectors
# from event_loop import EventLoop
# from future import Future
#
# class PyAsync(object):
#
#     def __init__(self):
#         self.loop = EventLoop()
#         self.events_listen = [sys.stdin]
#         self.flag = False
#
#     def get_event_loop(self):
#         return self.loop
#
#     def coroutine(self, func):
#         def wrap(*args, **kwargs):
#
#             while True:
#                 f = Future()
#                 print('----start---------')
#                 def on_read2(event):
#                     print('on_read2')
#                     junk = event.readline()
#                     print('junk', junk)
#                     f.set_result(junk)
#
#                 if self.flag == False:
#                     self.flag = True
#                     self.loop.register_event(sys.stdin, on_read2)
#
#                 func(*args, **kwargs)
#                 print('fff')
#                 a = yield f
#                 print('after yided', a)
#
#         return wrap
