"""
Problem Statement

You are given a string S.
The string consists of lowercase alphabets.

Your task is to find top three most common characters in the string S.

Input Format

Single line containing string S.

Constraints

3<len(S)<104
Output Format

Print the most common characters along with their count of occurences in three lines.
Output must sorted in descending order of count of occurences.
If count of occurences is same then sort in ascending order of characters.

Sample Input

aabbbccde
Sample Output

b 3
a 2
c 2
Explanation

b is occuring 3 times. Hence, it is printed first.
Both a and c occur 2 times. So, a is printed in second line and c in third line because in ascending order of alphabets a comes ahead of c.

Note: The string S has at least 3 distinct characters.
"""
from collections import Counter

s = raw_input()
l = list(s)
c = Counter(l)
index = 0
l = c.most_common(3)
count = 0
is_equal = True
for i in l:
    print count, i[1]
    if index > 0 and count != i[1]:
        is_equal = False
        break
    else:
        count = i[1]
    index += 1
if is_equal:
    l.sort()
for i in l:
    print "".join("%s %s" % i)