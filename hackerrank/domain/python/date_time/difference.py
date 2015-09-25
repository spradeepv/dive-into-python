"""
Problem Statement

Timestamps are given in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the timezone. See sample below for details.

Task
Given 2 timestamps, print the absolute difference (in seconds) between them.

Input Format
First line contains T representing T testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Output Format
Print the absolute difference (t1?t2) in seconds.

Constraints
It is guaranteed that input contains only valid timestamps and the year can reach up to 3000.

Sample Input

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000
Sample Output

25200
88200
"""
from datetime import timedelta, tzinfo, datetime

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(minutes=offset)
        hours, minutes = divmod(offset, 60)
        self.__name = '<%+03d%02d>%+d' % (hours, minutes, -hours)
    def utcoffset(self, dt=None):
        return self.__offset
    def tzname(self, dt=None):
        return self.__name
    def dst(self, dt=None):
        return timedelta(0)
    def __repr__(self):
        return 'FixedOffset(%d)' % (self.utcoffset().total_seconds() / 60)

t = int(raw_input())
for i in range(t):
    s1 = raw_input()
    day, date, month, year, time, ts = s1.split()
    hr, minute, sec = time.split(":")
    dt_1 = datetime.strptime(year+' '+month+' '+date+' '+hr+':'+ minute+':'+sec,"%Y %b %d %H:%M:%S")
    offset = int(ts[-4:-2])*60 + int(ts[-2:])
    if ts[0] == "-":
        offset = -offset
    dt_1 = dt_1.replace(tzinfo=FixedOffset(offset))

    s2 = raw_input()
    day, date, month, year, time, ts = s2.split()
    hr, minute, sec = time.split(":")
    dt_2 = datetime.strptime(year+' '+month+' '+date+' '+hr+':'+ minute+':'+sec,"%Y %b %d %H:%M:%S")
    offset = int(ts[-4:-2])*60 + int(ts[-2:])
    if ts[0] == "-":
        offset = -offset
    dt_2 = dt_2.replace(tzinfo=FixedOffset(offset))

    print abs(int((dt_1 - dt_2).total_seconds()))
