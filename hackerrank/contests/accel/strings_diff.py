"""
Given 2 strings, A and B, find the number of substrings of A that differ
from B by exactly 1 character.

Input Format
------------

A single line containing 2 space-separated strings, A and B, respectively.

Constraints
-----------
0<|A|,|B|<10e6
All characters of A and B are lower case.

Output Format
-------------
Print a single integer denoting the number of substrings of A that differ
from B by exactly 11 character.

Sample Input
------------
abbab aba

Sample Output
-------------
2

Explanation
-------------
A="abbab", B="aba"
There are 3 substrings of AA having the same length as B: {"abb", "bba",
"bab"}
To convert "abb"->B"abb"->B, we must change the 3rd character from b to a.
To convert "bba"->B"bba"->B, we must change the 1st character from b to a.
To convert "bab"->B"bab"->B, all 3 characters must be changed (which breaks
the criterion set forth by the problem statement).

As 2 of the 3 substrings differ from BB by exactly 1 character, we print
2 on a new line.

Editorial
---------
Given a string S of length n, the Z Algorithm produces an array Z where Z[i]
is the length of the longest substring starting from S[i] which is also a
prefix of S, i.e. the maximum k such that S[j] = S[i+j] for all 0<=j<k.
This can be computed in O(n) time.
For more information refer to http://codeforces.com/blog/entry/3107
Let the two string be A,B as stated in the question Apply Z algorithm on BA
and B'A' and call the array returned by z algo as Z1 and Z2. Please note
here A' refers to the reverse of A. Now just see places where Z1[i]+Z2[
|A|+|B|-i] = |B|-1 for i >= n2
"""


def z_algo(input):
    n = len(input)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if (i <= r):
            # print i, r, l
            z[i] = min(r - i + 1, z[i - l])
        while (i + z[i] < n and input[z[i]] == input[i + z[i]]):
            z[i] += 1
        if (i + z[i] - 1 > r):
            l = i
            r = i + z[i] - 1
    return z


a, b = raw_input().split()
len_1 = len(a)
len_2 = len(b)
s = b + a
#print s
z1 = z_algo(s)
#print z1

s_rev = b[::-1] + a[::-1]
#print s_rev
z2 = z_algo(s_rev)
#print z2

ans = 0
for i in range(len_2, len_1 + 1):
    if z1[i] + z2[len_1 + len_2 - i] == len_2 - 1:
        ans += 1
print ans
