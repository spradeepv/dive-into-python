"""
Task

You are given two values a and b.
Your task is to do integer division and print a/b.

Input Format

First line contains, number of testcases T.
Next T line contains, space separated values of a and b.

Constraints

0<T<10
Output Format

Print value of a/b.
In case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note:
For integer division in Python 3 use //.
"""
from __future__ import division

t = int(raw_input())
for i in range(t):
    a, b = raw_input().split()
    try:
        c = int(a)//int(b)
        print c
    except ZeroDivisionError as zero_error:
        print "Error Code:", zero_error.message
    except ValueError as value_error:
        print "Error Code:", value_error.message
