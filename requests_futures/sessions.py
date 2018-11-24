# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/23 
@desc:
https://github.com/ross/requests-futures
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import partial
from requests import Session


class FuturesSession(Session):

    def __init__(self, max_workers=8, session=None, *args, **kwargs):
        super(FuturesSession, self).__init__(*args, **kwargs)

        executor = ThreadPoolExecutor(max_workers=max_workers)

        self.executor = executor
        self.session = session

    def request(self, *args, **kwargs):
        """
        Maintains the existing api for Session.request
        :param args:
        :param kwargs:
        :return:
        """
        if self.session:
            func = self.session.request
        else:
            # avoid calling super to not break pickled method
            func = partial(Session.request, self)

        s = self.executor.submit(func, *args, **kwargs)
        return s
