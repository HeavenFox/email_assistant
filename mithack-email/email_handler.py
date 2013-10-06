import webapp2
import logging

from actions import dispatcher

from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

class EmailHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info('Got request!')
        action = dispatcher.dispatch(mail_message)

        reply = action.act()

        if reply:
            reply.send()
            logging.info('Replied.')
        else:
            logging.info('No reply')

app = webapp2.WSGIApplication([EmailHandler.mapping()], debug=True)
