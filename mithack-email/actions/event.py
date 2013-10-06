from apiclient.discovery import build
from google.appengine.ext import webapp
from oauth2client.appengine import OAuth2Decorator
import time

# decorator = OAuth2Decorator(
#   client_id='348540417497.apps.googleusercontent.com',
#   client_secret='motfNfjiaxFaEmkBRWKurzXA',
#   scope='https://www.googleapis.com/auth/calendar')

# service = build('calendar', 'v3')

# class MainHandler(webapp.RequestHandler):

#     @decorator.oauth_required
#     def get(self):
#         # Get the authorized Http object created by the decorator.
#         http = decorator.http()
#         # Call the service using the authorized Http object.
#         request = service.events().list(calendarId='primary')
#         response = request.execute(http=http)

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

# class AddEvent(webapp2.RequestHandler):
#     @decorator.oauth_aware
#     def post(self):
#         if decorator.has_credentials():
#             event_name = self.request.get('event-name')
#             some_event = {
#                     'summary': self.event.name,
#                     'start': self.start_format,
#                     'end': self.end_format,
#                     'location': self.event.location
#             }
#             http = decorator.http()
#             # Using 'primary' will insert the event for the current user
#             request = service.events().insert(calendarId='primary', body=some_event)
#             inserted = request.execute(http=http)
#             self.response.write(json.dumps(inserted))
#         else:
#             self.response.write(json.dumps({'error': 'No credentials'}))

#     def __init__(self, event):
#         self.event = event
#         self.start_format = time.strftime('%b %d, %Y %H:%M', event.start)
#         self.end_format = time.strftime('%b %d, %Y %H:%M', event.end)

