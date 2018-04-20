# coding: utf-8

"""
FriendFeed 使用的基础 Web 框架，包含了 Tornado 的大多数重要的功能
"""

class RequestHandler(object):
    """
    处理请求，支持 GET/POST 等操作。
    r = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World aas</h1>'
    """
    SupportedMethods = ("GET", "HEAD", "POST", "DELETE", "PUT", "OPTIONS")

    def __init__(self, application):
        self.application = application
        self.response = 'HTTP/1.1 200 OK\r\n'
        self.headers = {}

    def head(self):
        pass

    def route(self):
        pass

    def set_header(self, name, value):
        self.headers.update({
            name: value
        })

    def finish(self, chunk=None):
        """Finishes this response, ending the HTTP request."""
        header = ''
        end = '\r\n'
        for key, value in self.headers.items():
            s = '{}: {}'.format(key, value) + end
            header += s

        if header:
            header += '\r\n'

        if chunk is not None:
            self.response += header + chunk

        return self.response.encode()


class _ApplicationRouter(object):

    def __init__(self, application, rules=None):
        self.application = application
        self.rules = []
        if rules:
            self.add_rules(rules)

    def add_rules(self, rules):
        """
        rules: [
            (r"/", MainHandler),
        ])
        :param rules:
        :return:
        """
        for rule in rules:
            if isinstance(rule, (tuple, list)):
                assert len(rule) in (2, 3,4)
                if isinstance(rule[0], str):
                    pass
                else:
                    pass

    def process_rule(self, rule):
        pass

class Application(object):

    def __init__(self, handlers=None):
        """
         handlers:   [
            (r"/", handler类),
        ]
        """
        self.named_router = {}
        if handlers is not None:
            self.add_handlers(".*$", handlers)

    def add_handlers(self, host_pattern, host_handlers):
        for spec in host_handlers:
            self.named_router.update({
                spec[0]: spec[1]
            })

