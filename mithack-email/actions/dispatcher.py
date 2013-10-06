from actions import *
from context import Context
import re
import logging

def dispatch(email):
    ctx = Context(email)
    logging.info(email.body.decode())

    # calendar
    cal_match = re.search(r'put (.+) on (\w+ )?(calendar|schedule)', email.body.decode())
    if cal_match:
        return NewEventAction(ctx)

    # appointment
    appointment_match = re.search(r'(^schedule .+|find .+time)', email.body.decode())
    if appointment_match:
        return NewAppointmentAction(ctx)

    return InvalidAction(ctx)
