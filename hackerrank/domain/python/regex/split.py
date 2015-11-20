"""
Problem Statement

re.split()

It splits the string by occurrence of a pattern.

Code

>> import re
>> re.split("-","+91-011-2711-1111")
['+91', '011', '2711', '1111']
Task
You are given a string S, containing , and/or . and 0-9 digits.
Your task is to re.split() all , and . symbols.

Input Format

Single line containing string S.

Output Format

Print the numbers obtained after splitting in separate lines.

Sample Input

100,000,000.000
Sample Output

100
000
000
000
"""
import re

l = filter(None, re.split("\.", raw_input()))
for i in l:
    print "\n".join(filter(None, re.split(",", i)))
