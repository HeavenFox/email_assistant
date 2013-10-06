import re

from collections import namedtuple

Request = namedtuple('Request', ['command', 'email', 'reference'])

class RequestParser(object):
    def parse(self, email):
        body = email.body.decode()

        splitted = re.split('-{4,}[^-]+-{4,}', body, maxsplit=1)
        command = None
        body = None
        if len(splitted) > 1:
            command, body = splitted
        else:
            command = body = splitted

        ref = re.search('_mew_ref_ (\w+)', body)
        if ref:
            ref = ref.group(1)

        return Request(command, body, ref)



