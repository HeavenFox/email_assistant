from google.appengine.api.mail import EmailMessage
import nlp
import time
import logging

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
        filtered_reference = "".join(i for i in self.context.referenced_email if ord(i)<128)
        text = "\n".join(filtered_reference.splitlines()[8:-5])
        logging.info(text)
        subject = email.subject

        subject = subject.replace('Fwd:','').replace('Re:', '').strip()

        start_time, end_time = nlp.time_parser.parse(text)
        event_name = ' - '.join(nlp.topic_parser.generate_topics(subject, text))
        loc = nlp.location_parser.parse(text)

        def time_format(t):
            if not t:
                return "N/A"
            return time.strftime('%b %d, %Y %H:%M', t)

        reply = self.build_reply(self.context.email)
        reply.body = 'We have created the event for you. \n'
        reply.body += '\n'
        reply.body += (' * Name: ' + str(event_name) + '\n')
        reply.body += (' * Start: ' + time_format(start_time) + '\n')
        reply.body += (' * End: ' + time_format(end_time) + '\n')
        reply.body += (' * Location: ' + str(loc) + '\n')

        return reply

class NewAppointmentAction(Action):
    def act(self):
        reply = self.build_reply(self.context.email)
        reply.body = 'We have scheduled the dinner for ya.'
        return reply
