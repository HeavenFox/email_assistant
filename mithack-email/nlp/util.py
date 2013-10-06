import re
import parsedatetime as pdt
import time_parser

def combine_intervals(intvs):
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

def parse_single_time(email, interval):
    pass
    parser = pdt.Calendar()
    types = [x[2] for x in interval]
    if time_parser.DAY_OF_WEEK in types and time_parser.DATE in types:
        interval = filter(lambda x: x[2] != time_parser.DAY_OF_WEEK, interval)
    types = [x[2] for x in interval]
    target = ""
    if time_parser.DAY_OF_WEEK in types:
        tlst = filter(lambda x: x[2] == time_parser.DAY_OF_WEEK, interval)
        target += (email[tlst[0][0]:tlst[0][1]] + " ")
    if time_parser.DATE in types:
        tlst = filter(lambda x: x[2] == time_parser.DATE, interval)
        target += (email[tlst[0][0]:tlst[0][1]] + " ")
    if time_parser.TIME in types:
        tlst = filter(lambda x: x[2] == time_parser.TIME, interval)
        target += (email[tlst[0][0]:tlst[0][1]] + " ")
    result, succ = parser.parse(target)
    if succ == 0:
        return None
    return result



# Given [(st, ed, type)] 
# Concat adjacent date
def combine_times(intervals):
    res = []
    i = 0
    while i < len(intervals):
        j = i
        t = [intervals[i]]
        while j < len(intervals) - 1:
            _, ed, _ = intervals[j]
            st, _, _ = intervals[j+1]
            if st - ed < DATE_CONCAT_LIMIT:
                t.append(intervals[j+1])
            else:
                break
        res.append(t)
    return res

# Given a String of time 
# Single Point of Tim [s1, t1, date]
# Date, time - time
# Date, time - Date. time
def parse_interval(email, interval):

    intv = []
    if timestr.find("and") != -1:
        intv = timestr.split("and")
    elif timestr.find("to") != -1:
        intv = timestr.split("to")
    elif timestr.find("-") != -1:
        intv = timestr.split("-")

    if len(intv) < 2:
        return None

    tbegin = parse_time(intv[0])
    


    






