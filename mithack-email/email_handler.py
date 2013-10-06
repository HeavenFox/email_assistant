import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

class EmailHandler(InboundMailHandler):
    def receive(self, mail_message):
        pass

app = webapp2.WSGIApplication([EmailHandler.mapping()], debug=True)
