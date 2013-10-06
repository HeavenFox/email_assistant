from __future__ import print_function
import time_parser

s = open('time_parser_test.txt','r').read()


interval = time_parser.tag_dates(s)


print(s)
import itertools

gen = itertools.chain(*interval)

try:
    last = gen.next()
except:
    last = None

for i in xrange(len(s)):
    if i == last:
        print('---', end='')
        try:
            last = gen.next()
        except:
            pass
    print(s[i], end='')

