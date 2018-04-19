# coding: utf-8
import selectors
import select
import sys

class EventLoop(object):

    def __init__(self):
        self.events_to_listen = []
        self.callbacks = {}
        self.timeout = None

    def register_event(self, event, callback):
        self.events_to_listen.append(event)
        self.callbacks[event] = callback

    def unregister_event(self, event):
        self.events_to_listen.remove(event)
        del self.callbacks[event]

    def _process_events(self, events):
        for event in events:
            self.callbacks[event](event)

    def start_loop(self):
        while True:
            pass
            # 调用 select 函数，阻塞等待
            events = self.events_to_listen
            readable, writeable, exceptional = select.select(events, [], [])
            if len(readable) > 0:
                self._process_events(readable)

    def close(self):
        pass
