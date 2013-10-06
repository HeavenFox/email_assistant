import re
import parsedatetime as pdt
import time_parser
import time


# Given a string of the email content, an exact match of text
# Return the conbined paragraph text that contains this text

# when where what
# long paragraph

SHORT_SENTENCE_LIMIT = 60
DATE_CONCAT_LIMIT = 5


def match_date_paragraph(email, date):
    paragraphs = email.split('\n')
    paragraphs = [line.strip() for line in paragraphs]

    i = 0
    result = ""
    while i < len(paragraphs) and paragraphs[i].find(date) == -1:
        i += 1

    # not found
    if i == len(paragraphs):
        return None

    if len(paragraphs[i] > SHORT_SENTENCE_LIMIT):
        return paragraphs[i]
    else:
        u = i
        d = i
        while u > 0 and len(paragraphs[u]) > 0 and len(paragraphs[u] <= SHORT_SENTENCE_LIMIT):
            u -= 1
        while d < len(paragraphs) and len(paragraphs[d]) > 0 and len(paragraphs[d] <= SHORT_SENTENCE_LIMIT):
            d += 1
        return "\n".join(paragraphs[u:d])

# take a list of intervals
def parse_single_time(email, interval, basetime = None):
    # import pdb; pdb.set_trace()
    parser = pdt.Calendar()
    interval = filter(lambda x: x[2] != time_parser.TIME_INTERVAL and x != time_parser.DATE_INTERVAL, interval)
    types = [x[2] for x in interval]
    if time_parser.DAY_OF_WEEK in types and time_parser.DATE in types:
        interval = filter(lambda x: x[2] != time_parser.DAY_OF_WEEK, interval)
    types = [x[2] for x in interval]
    target = ""
    if time_parser.DAY_OF_WEEK in types:
        tlst = filter(lambda x: x[2] == time_parser.DAY_OF_WEEK, interval)
        target += (email[tlst[0][0]:tlst[0][1]] + ", ")
    if time_parser.DATE in types:
        tlst = filter(lambda x: x[2] == time_parser.DATE, interval)
        target += (email[tlst[0][0]:tlst[0][1]])
    if time_parser.TIME in types:
        tlst = filter(lambda x: x[2] == time_parser.TIME, interval)
        target += (" at " + email[tlst[0][0]:tlst[0][1]])
    result, succ = parser.parse(target.strip(), basetime)
    if succ == 0:
        return None
    if type(result) == type(tuple()):
        result = time.struct_time(result)
    return result

def parse(text):
    # try:
    intv = time_parser.tag_dates(text)
    types = [x[2] for x in intv]
    if time_parser.TIME_INTERVAL in types:
        return parse_interval(text, intv)
    t = parse_single_time(text, intv)
    if t is None:
        return None, None
    tnext = time.mktime(t) + 3600
    tnext = time.localtime(tnext)

    return t, tnext
# except:
    #     return None

def parse_interval(email, interval):

    minl = 1 << 20
    maxr = -1
    for l,r,_ in interval:
        minl = min(l, minl)
        maxr = max(r, maxr)
    timestr = email[minl:maxr]

    if timestr.find(" and ") != -1 or timestr.find(" to ") != -1:
        if timestr.find(" and ") != -1:
            strarr = timestr.split(" and ")
        else:
            strarr = timestr.split(" to ")
        intv0 = time_parser.tag_dates(timestr[0]) 
        intv1 = time_parser.tag_dates(timestr[1]) 
        return parse_single_time(timestr[0], intv[0]), parse_single_time(timestr[1], intv[1])

    elif timestr.find("-") != -1:
        intv = time_parser.tag_dates(timestr)
        basetime = parse_single_time(email, intv)
        intv = filter(lambda x: x[2] == time_parser.TIME_INTERVAL or x == time_parser.DATE_INTERVAL, intv)
        timestr = email[intv[0][0] : intv[0][1]]
        tarray = timestr.split("-")
        tintv = time_parser.tag_dates(tarray[1])
        endtime = parse_single_time(tarray[1], tintv, basetime) 
        ampm = "am"
        if endtime.tm_hour > 12:
            ampm = "pm"
        tintv = time_parser.tag_dates(tarray[0] + ampm)
        starttime = parse_single_time(tarray[0]+ampm, tintv, basetime)

        return starttime, endtime



# Given [(st, ed, type)] 
# Concat adjacent date
def combine_times(intervals):
    res = []
    i = 0
    print intervals
    # import pdb; pdb.set_trace()
    while i < len(intervals):
        j = i
        t = [intervals[i]]
        while j < len(intervals) - 1:
            ed = intervals[j][1]
            st = intervals[j+1][0]
            if st - ed < DATE_CONCAT_LIMIT:
                t.append(intervals[j+1])
                j += 1
            else:
                break
        res.append(t)
        i = j + 1
    return res

# Given a String of time 
# Single Point of Tim [s1, t1, date]
# Date, time - time
# Date, time - Date. time

