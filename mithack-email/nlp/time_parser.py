import re
from util import combine_intervals

def tag_dates(s):
	res = [re.compile(r'(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|wed|thu|fri|sat|sun)'),
		re.compile(r'(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* \d{1,2}((,| )\d{2,4})?'),
		re.compile(r'(\d{1,2}:?\d{1,2} ?(a|p)m?)|(\d{1,2}(a|p)m?)')]

	intervals = []

	for regex in res:
		for match in regex.finditer(s, re.I):
			intervals.append((match.start(), match.end()))

	return combine_intervals(intervals, s, lambda x: len(x) < 3)
