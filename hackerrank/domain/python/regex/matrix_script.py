"""
Problem Statement

Neo has a complex matrix script. The matrix script is a N X M grid of
strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,
$,%,&).

To decode the script, Neo needs to read each column and select only the
alphanumeric characters and connect them. Neo reads the column from top to
bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the
decoded script, then Neo replaces them with a single space ' ' for better
readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N (rows) and M (columns)
respectively.
The next N lines contain the row elements of the matrix script.

Constraints

0<N,M<100

Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input

7 3
Tsi
h%x
i #
sM
$a
#t%
ir!
Sample Output

This is Matrix#  %!
Explanation

The decoded script is:

This$#is% Matrix#  %!
Neo replaces the symbols or spaces between two alphanumeric characters with
a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!
"""
import re


def input():
    n, m = map(int, raw_input().split())
    l = []
    for i in range(n):
        l.append(raw_input())
    s = ''
    for i in range(m):
        for j in range(n):
            s += l[j][i]
    return s


#s = input()
s="This$#is% Matrix#  %!"
print s
pattern_1 = r'[a-zA-Z0-9]([!@#$%&\s]+)[a-zA-Z0-9]'
#pattern_1 = "(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])"
print re.findall(pattern_1, s)
for match in re.finditer(pattern_1, s):
    print match.groups()
    s = s.replace(str(match.group(1)), ' ', 1)
print s
