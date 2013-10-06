import request

class Context(object):
    def __init__(self, email):
        self.email = email
        self.command, self.referenced_email, self.ref = request.RequestParser.parse(email)
