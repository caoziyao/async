# coding: utf-8

class RequestHandler(object):

    def __init__(self):
        pass

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
        handlers = list(handlers or [])
        self.wildcard_router = _ApplicationRouter(self, handlers)


