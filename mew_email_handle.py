import logging
import webapp2
import json
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail

class EchoHtmlHandler(InboundMailHandler):
  def receive(self, message):
    for content_type, body in message.bodies('text/html'):
      thebody = body.decode()
      
    mail.send_mail(sender = message.to,
                   to = message.sender,
                   subject ="Re: " + message.subject, 
                   body = thebody)
class EchoTextHandler(InboundMailHandler):
  def receive(self, message):
    for content_type, body in message.bodies('text/plain'):
      thebody = body.decode()
      
    mail.send_mail(sender = message.to,
                   to = message.sender,
                   subject ="Re: " + message.subject, 
                   body = thebody)

                   
echohtml = webapp2.WSGIApplication([EchoHtmlHandler.mapping()], debug = True)
echotext = webapp2.WSGIApplication([EchoTextHandler.mapping()], debug = True)