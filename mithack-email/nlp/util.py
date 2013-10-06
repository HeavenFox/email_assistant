import re

def combine_intervals(intvs, st, insig_func):
	intervals = sorted(intvs)
	combined_intervals = []
	last_s, last_t = intervals[0]
	for s, t in intervals[1:]:
		if s > last_t:
			if insig_func(st[last_t:s]):
				last_t = t
			else:
				combined_intervals.append((last_s, last_t))
				last_s = s
				last_t = t
		else:
			last_t = t

	combined_intervals.append((last_s, last_t))
	return combined_intervals

