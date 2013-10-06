from apiclient.discovery import build
from google.appengine.ext import webapp
from oauth2client.appengine import OAuth2Decorator

# decorator = OAuth2Decorator(
#   client_id='mithack-email',
#   client_secret='your_client_secret',
#   scope='https://www.googleapis.com/auth/calendar')

# service = build('calendar', 'v3')

# class MainHandler(webapp.RequestHandler):

#   @decorator.oauth_required
#   def get(self):
#     # Get the authorized Http object created by the decorator.
#     http = decorator.http()
#     # Call the service using the authorized Http object.
#     request = service.events().list(calendarId='primary')
#     response = request.execute(http=http)

class Event:
    def __init__(self, name, location, start, end):
        self.name = name
        self.location = location
        self.start = start
        self.end = end

class EventAction(object):
    def act(self):
        pass

    def followup(self, command):
        pass
