"""
Problem Statement

You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string S.

Constraints

0<len(S)<1000
Output Format

Output the sorted string S.

Sample Input

Sorting1234
Sample Output

ginortS1324
Note:
a) Using join, for or while anywhere in your code, even as substrings,
will result in a score of 0.
b) You can only use one sorted function in your code. A 0 score will be
awarded for using sorted more than once.

Hint: Success is not the key, but key is success.
"""
from __future__ import print_function

def func(x):
    if x.isalpha():
        if x.isupper():
            return (ord(x)-ord('A'))
        else:
            return (ord(x)-ord('a'))-30
    else:
        if int(x) % 2 == 0:
            return 60+int(x)
        else:
            return 30+int(x)

def compare(x, y):
    if x.islower() and y.isdigit():
        return -1
    if x.isupper() and y.isdigit():
        return -1
    if x.isdigit() and y.islower():
        return 1
    if x.isdigit() and y.isupper():
        return 1
    elif x.islower() and y.isupper():
        return -1
    if x.isupper() and y.islower():
        return 1
    elif x.islower() and y.islower():
        return ord(x) - ord(y)
    elif x.isupper() and y.isupper():
        return ord(x) - ord(y)
    elif x.isdigit() and y.isdigit():
        if int(x) % 2 != 0 and int(y) % 2 != 0:
            return int(x) - int(y)
        elif int(x) % 2 != 0 and int(y) % 2 == 0:
            return -1
        elif int(x) % 2 == 0 and int(y) % 2 != 0:
            return 1
        elif int(x) % 2 == 0 and int(y) % 2 == 0:
            return int(x) - int(y)


s = raw_input()
l = list(s)
#l.sort(cmp=compare)
#l.sort(key=func)
map(lambda x: print(x, end=''), sorted(s, key=func))
# print(str(l)[1:-1].replace(',', '').replace(',', '').replace('\'', '').replace(
#     ' ', ''))
