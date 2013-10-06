from google.appengine.api.mail import EmailMessage
import nlp

class Action(object):
    def __init__(self, context):
        self.context = context;

    def act(self):
        pass

    def build_reply(self, email):
        reply = EmailMessage(to=email.sender, sender='noreply@mithack-email.appspotmail.com', subject='Re: ' + email.subject, headers={'In-Reply-To': email.original['message-id']})

        return reply


class InvalidAction(Action):
    def act(self):
        reply = self.build_reply(self.context.email)
        reply.body = 'Sorry but I cannot understand your command.'
        return reply


class NewEventAction(Action):
    def act(self):
        email = self.context.email
        text = email.body.decode()
        subject = email.subject

        start_time, end_time = nlp.time_parser.parse(text)
        event_name = ' - '.join(nlp.topic_parser.generate_topics(subject, text))
        loc = nlp.location_parser.parse(text)

        reply = self.build_reply(self.context.email)
        reply.body = 'We have created the event for ya.'
        return reply

class NewAppointmentAction(Action):
    def act(self):
        reply = self.build_reply(self.context.email)
        reply.body = 'We have scheduled the dinner for ya.'
        return reply
