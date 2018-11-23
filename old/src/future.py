# coding: utf-8

class Future(object):
    def __init__(self):
        self.result = None
        self._callbacks = []

    # 回调
    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            print('len of callback', len(self._callbacks), fn)
            fn(self)


