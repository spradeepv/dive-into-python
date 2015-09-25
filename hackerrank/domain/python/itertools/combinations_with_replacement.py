"""
Task

You are given a string S.
Your task is to print all possible combinations with replacement of size k, of the string in lexicographic sorted order.

Input Format

Single line containing space separated , string S and value k.

Constraints

0<N<10
0<k?len(S)
String contains only UPPERCASE characters.

Output Format

Print combinations with replacement of string S in separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
from itertools import combinations_with_replacement

s, k = raw_input().split()
k = int(k)
l = []
l[:0] = s
l.sort()
s = "".join(l)
for tup in list(combinations_with_replacement(s, k)):
    print "".join(tup)
