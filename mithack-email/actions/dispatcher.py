from actions import *
from context import Context
import re
import logging

def dispatch(email):
    ctx = Context(email)
    logging.info(email.body.decode())

    command = ctx.command

    # calendar
    cal_match = re.search(r'put (.+) on (\w+ )?(calendar|schedule)', command)
    if cal_match:
        return NewEventAction(ctx)

    # appointment
    appointment_match = re.search(r'(^schedule .+|find .+time)', command)
    if appointment_match:
        return NewAppointmentAction(ctx)

    return InvalidAction(ctx)
