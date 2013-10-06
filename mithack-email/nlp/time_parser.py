import re
# from util import combine_intervals

DAY_OF_WEEK = 0
DATE = 1
DATE_INTERVAL = 2
TIME = 3
TIME_INTERVAL = 4

def tag_dates(s):
    regs = {
        DAY_OF_WEEK: [re.compile(r'(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun)', re.I)],
        DATE: [re.compile(r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* \d{1,2}((,| )\d{2,4})?', re.I)],
        DATE_INTERVAL: [],
        TIME: [re.compile(r'(\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(a|p)m?)',re.I)],
        TIME_INTERVAL: [re.compile(r'((\d{1,2}:?\d{1,2} ?(am?|pm?)?)|(\d{1,2}(am?|pm?)?))( ?(to|-) ?)((\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(a|p)m?))', re.I)]
    }

    intervals = []

    s = "e " + s

    # print s
    for typ, regexes in regs.iteritems():
        for regex in regexes:
            matches = list(regex.finditer(s, re.I))
            # print matches
            for match in matches:
                intervals.append((match.start() - 2, match.end() - 2, typ))

    return combine_intervals(intervals)

def combine_intervals(intvs):
    # import pdb; pdb.set_trace()
    intervals = sorted(intvs)
    combined_intervals = []
    last_s, last_t, last_type = intervals[0]
    for s, t, lt in intervals[1:]:
        if s <= last_t:
            last_t = t
            last_type = max(lt, last_type)
        else:
            combined_intervals.append((last_s, last_t, last_type))
            last_s = s
            last_t = t
            last_type = lt

    combined_intervals.append((last_s, last_t, last_type))
    return combined_intervals


