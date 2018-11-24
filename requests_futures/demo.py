# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/23 
@desc:
"""

import requests
import time
from threading import Event, Thread
from requests import Session

req = Session()
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[p] Producing %s...' % n)
#         r = c.send(n)
#         print('[p] Consumer return: %s' % r)
#     c.close()


# produce(c)
queue = []
# c1_running = False
# c2_running = False
n = (None, 'c1')


class Worker(Thread):

    def __init__(self, name, url):
        Thread.__init__(self)
        self.name = name
        self.url = url
        self.res = None

    def run(self):
        print('run', self.name)
        try:
            # r = c1.send((self.url, self.name))
            r = req.get(self.url)
            r = r.status_code
        except Exception as e:
            print(e)
            r = None
        self.res = r

    def result(self):
        return self.res


def consumer():
    r = ''
    while True:
        # if n[1] == 'c1':
        #     c1_running = False
        # if n[1] == 'c2':
        #     c2_running = False

        n = yield r
        # if n[1] == 'c1':
        #     c1_running = True
        # if n[1] == 'c2':
        #     c2_running = True

        if not n[0]:
            return
        print('[c] Consuming ..', n)
        time.sleep(1)
        r = '200 OK ' + n[0]


ths = []


class Future(object):

    def get(self, url):
        """

        :param url:
        :return:
        """
        # time.sleep(1)
        # print('ok', url)
        print('[p] Producing ...', url)
        w = Worker('c1', url)

        ths.append(w)
        # r = c1.send((url, 'c1'))
        # print(r)
        return w

        # if c1_running:
        #     pass
        # else:
        #     w = Worker('c1', url)
        #     w.run()
        #     # r = c1.send((url, 'c1'))
        #     # print(r)
        #     return w
        #
        # if c2_running:
        #     pass
        # else:
        #     w = Worker('c2', url)
        #     w.run()
        #     # r = c2.send((url, 'c2'))
        #     # print(r)
        #     return w


c1 = consumer()
# c2 = consumer()
c1.send(None)
# c2.send(None)

session = Future()

f1 = session.get('http://www.baidu.com')
f2 = session.get('http://www.qq.com')
f3 = session.get('http://www.qq3.com')
f4 = session.get('http://www.qq4.com')
f5 = session.get('http://www.qq5.com')
f6 = session.get('http://www.qq6.com')

for th in ths:
    th.start()

time.sleep(1)

r1 = f1.result()
r2 = f2.result()
r3 = f3.result()
r4 = f4.result()
r5 = f5.result()
r6 = f6.result()

print('r1', r1)
print('r2', r2)
print('r3', r3)
print('r4', r4)
print('r5', r5)
print('r6', r6)
