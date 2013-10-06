from google.appengine.api.mail import EmailMessage
import nlp
import time

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
        text = self.context.referenced_email
        subject = email.subject

        subject = subject.replace('Fwd:','').replace('Re:', '').strip()

        start_time, end_time = nlp.time_parser.parse(text)
        event_name = ' - '.join(nlp.topic_parser.generate_topics(subject, text))
        loc = nlp.location_parser.parse(text)

        def time_format(t):
            return time.strftime('%b %d, %Y %H:%M', t)

        reply = self.build_reply(self.context.email)
        reply.body = 'We have created the event for you. \n'
        reply.body += '\n'
        reply.body += (' * Name: ' + event_name + '\n')
        reply.body += (' * Start: ' + str(start_time) + '\n')
        reply.body += (' * End: ' + str(end_time) + '\n')
        reply.body += (' * Location: ' + (loc) + '\n')

        return reply

class NewAppointmentAction(Action):
    def act(self):
        reply = self.build_reply(self.context.email)
        reply.body = 'We have scheduled the dinner for ya.'
        return reply
