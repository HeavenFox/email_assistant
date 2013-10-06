from google.appengine.ext import ndb

class ConversationContextEntry(ndb.Model):
    state = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
