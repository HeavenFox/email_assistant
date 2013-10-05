import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail

class MewEmailHandler(InboundMailHandler):
  def receive(self, message):
    mail.send_mail(sender = message.to,
                   to = message.sender,
                   subject ="Re: " + message.subject, 
                   body = "Success!")
                   
app = webapp2.WSGIApplication([MewEmailHandler.mapping()], debug = True)