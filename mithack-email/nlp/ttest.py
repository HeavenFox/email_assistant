import time_parser
import util

s = ["Wednesday, October 2nd at 1:30pm-2:30pm at Cornell University Career Services, 201 Carpenter Hall"]
s.append("Wednesday 1:30pm to Thursday 2:30am")
s.append("Please complete the following by Friday September 27th at 5:00pm")
s.append("Friday: 3-4pm")

for string in s:
    print util.parse(string)
