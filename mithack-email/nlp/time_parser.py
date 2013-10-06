import re
from util import combine_intervals

DAY_OF_WEEK = 0
DATE = 1
DATE_INTERVAL = 2
TIME = 3
TIME_INTERVAL = 4

def tag_dates(s):
    regs = {
        DAY_OF_WEEK: [re.compile(r'(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun)')],
        DATE: [re.compile(r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* \d{1,2}((,| )\d{2,4})?')],
        DATE_INTERVAL: [],
        TIME: [re.compile(r'(\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(a|p)m?)')],
        TIME_INTERVAL: [re.compile(r'((\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(am?|pm?)?))( ?(to|-) ?)((\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(a|p)m?))')]
    }

    intervals = []

    for typ, regexes in regs.iteritems():
        for regex in regexes:
            for match in regex.finditer(s, re.I):
                intervals.append((match.start(), match.end(), typ))

    return intervals
