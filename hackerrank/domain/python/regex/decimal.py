"""
Problem Statement

re

A Regular expression (or RegEx) specifies a set of strings that matches it.

A regex is a sequence of characters that define a search pattern, mainly for the use in pattern matching with strings.


re.search()
It scans through string looking for the first location where the regex pattern produces a match.
It returns MatchObject instance or returns None if no position in the string matches the pattern. Code

>> import re
>> print bool(re.search(r"ly","similarly"))
True

re.match()
It only matches at the beginning of the string.
It returns MatchObject instance or returns None if the string does not match the pattern.
Code

>> import re
>> print bool(re.match(r"ly","similarly"))
False
>> print bool(re.match(r"ly","ly should be in the beginning"))
True
Task
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following:

> Number can start with +, - or . symbol.
    For example :
    ? +4.50
    ? -1.0
    ? .5
    ? -.7
    ? +.4
    ? -+4.5

> Number must contain alteast one decimal value.
    For example:
    ? 12.
    ? 12.0

> Number must have exactly one . symbol.
> Number must not give any exceptions when converted using float(N).

Input Format

First line contains, integer T, number of testcases.
Next T line contain, string N.

Constraints

0<T<10
Output Format

Output True or False for each textcase.

Sample Input

4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output

False
True
True
False
Explanation

4.0O0 : O is not a digit.
-1.00 : is valid.
+4.54 : is valid.
SomeRandomStuff : is not a number.
"""
import re
for _ in range(int(raw_input())):
    s = raw_input()
    try:
        f = float(s)
    except ValueError:
        print False
        continue
    print bool(re.match(r"[+-.]+[0-9]+$|[+-]*[0-9]+.[0-9]+$", s))