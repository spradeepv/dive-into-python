"""
Task

You are given a string S.
Your task is to print all possible combinations upto size k, of the string in
lexicographic sorted order.

Input Format

Single line containing space separated , string S and value k.

Constraints

0<N<10
0<k?len(S)
String contains only UPPERCASE characters.

Output Format

Print combinations of string S in separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations

s, k = raw_input().split()
k = int(k)
l = []
l[:0] = s
l.sort()
s = "".join(l)
for i in range(1, k+1):
    for tup in list(combinations(s, i)):
        print "".join(tup)

