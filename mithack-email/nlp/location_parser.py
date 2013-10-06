import re
import alchemyapi

def combine_intervals(intvs, st, insig_func):
    intervals = sorted(intvs)
    combined_intervals = []
    last_s, last_t = intervals[0]
    for s, t in intervals[1:]:
        if s <= last_t:
            if t > last_t:
                last_t = t
        else:
            if insig_func(st[last_t:s]):
                last_t = t
            else:
                combined_intervals.append((last_s, last_t))
                last_s = s
                last_t = t

    combined_intervals.append((last_s, last_t))
    return combined_intervals

def tag_location(s):
    api = alchemyapi.AlchemyAPI()
    entities = []
    for x in api.entities('text', s)[u'entities']:
        if x['type'] in ['Organization', 'Facility','City']:
            for match in re.finditer(x['text'], s):
                entities.append([match.start(0), match.end(0)])

    # Expand to include room no
    room_no_regex = re.compile(r'\d| ')
    for ent in entities:
        while ent[1] < len(s) and room_no_regex.match(s[ent[1]]):
            ent[1] += 1
        while ent[0] - 1 > 0 and room_no_regex.match(s[ent[0]]):
            ent[0] -= 1

    # Consolidate
    return combine_intervals(entities, s, lambda x: re.match(' *(,) *', x))


def parse(s):
    tags = tag_location(s)
    if len(tags) > 3 or len(tags) == 0:
        return None
    return s[tags[0][0]:tags[0][1]]




