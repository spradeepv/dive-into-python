"""
Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Constraints

0<len(S)<100
0<len(k)<len(S)
Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)
(1, 2)
(4, 5)
"""
import re

s = raw_input()
k = raw_input()

m = re.search(r'(a{2})?', s)
print m.groups()
print m.start(), m.end()
