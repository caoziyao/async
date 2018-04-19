# coding: utf-8

import web
import httpserver
import ioloop

def main_handler():
    pass


def main():
    port = 3005
    host = 'localhost'
    app = web.Application([
        (r"/", main_handler),
    ])
    http_server = httpserver.HTTPServer(app)
    http_server.listen(port, host)
    print('{}:{}'.format(host, port))
    ioloop.EventLoop.instance().start()


if __name__ == "__main__":
    main()

