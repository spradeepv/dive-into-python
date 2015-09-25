"""
Task

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format

Single line containing space separated , string S and value k.

Constraints

0<N<10
0<k?len(S)
String contains only UPPERCASE characters.

Output Format

Print permutations of string S in separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible permuatations of size 2 of ths string "HACK" are printed in lexicographic sorted order.
"""
from itertools import permutations

s, k = raw_input().split()
k = int(k)
l = []
l[:0] = s
l.sort()
s = "".join(l)
for tup in list(permutations(s, k)):
    print "".join(tup)
