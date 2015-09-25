"""
Task

You are given the date of the day. Your task is to find what day it is on that date.

Input Format

Single line containing space separated month, day and year in MM DD YYYY format.

Constraints

2000<year<3000
Output Format

Output the correct day.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

Day on 5th August 2015 is WEDNESDAY
"""
import calendar

m, d, y = map(int, raw_input().split())
calendar.setfirstweekday(calendar.MONDAY)
print calendar.day_name[calendar.weekday(y, m, d)].upper()