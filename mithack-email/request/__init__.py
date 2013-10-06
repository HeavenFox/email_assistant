from collections import namedtuple

Request = namedtuple('Request', ['command', 'reference'])

class RequestParser(object):
    def parse(self, email):
        pass
