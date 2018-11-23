# coding: utf-8

import sys
from src import web
from src import httpserver
from src import ioloop
from src import gen
from src.future import Future
from src.task import Task


def stdin_test(content):
    global flag
    loop = ioloop.IOLoop.instance()
    f = Future()
    print('----start---------')

    def on_read2(event):
        # global content
        print('on_read2')
        # junk = event.readline()
        # print('junk', junk)
        content = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World aas</h1>'
        # content += junk
        content = content.encode()
        loop.unregister_event(sys.stdin, flag='a')
        f.set_result(content)

    loop.register_event(sys.stdin, on_read2, flag='a')

    return f


class HelloWorldHandler(web.RequestHandler):

    @gen.coroutine
    def get(self, stream):
        print('get HelloWorldHandler')
        name = 'csy'
        self.set_header("Content-Type", "text/plain")
        # r = yield self.finish("hi {}!".format(name))
        content = self.finish("hi {}!".format(name))
        content = content.decode()
        r = yield stdin_test(content)

        print('r', r)
        print('stream', stream)
        stream.write(r)
        stream.close()
        # return r


def stdin_test2(content):
    global flag
    loop = ioloop.IOLoop.instance()
    f = Future()
    print('----start---------')

    def on_read2(event):
        # global content
        print('on_read2')
        # junk = event.readline()
        # print('junk', junk)
        content = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World bbb</h1>'
        # content += junk
        content = content.encode()
        loop.unregister_event(sys.stdin, flag='b')
        f.set_result(content)

    loop.register_event(sys.stdin, on_read2, flag='b')

    return f


class TestHandler(web.RequestHandler):

    @gen.coroutine
    def get(self, stream):
        print('get HelloWorldHandler')
        name = 'test'
        self.set_header("Content-Type", "text/plain")
        # r = yield self.finish("hi {}!".format(name))
        content = self.finish("hi {}!".format(name))
        content = content.decode()
        r = yield stdin_test2(content)

        print('r', r)
        print('stream', stream)
        stream.write(r)
        stream.close()
        # return r


# class TestHandler(web.RequestHandler):
#
#     @gen.coroutine
#     def get(self):
#         name = 'csy'
#         self.set_header("Content-Type", "text/plain")
#         r = self.finish("test {}!".format(name))
#         return r


def main():
    port = 3005
    host = 'localhost'
    app = web.Application([
        (r"/", HelloWorldHandler),
        (r"/test", TestHandler),
    ])
    http_server = httpserver.HTTPServer(app)
    http_server.listen(port, host)
    print('{}:{}'.format(host, port))
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
