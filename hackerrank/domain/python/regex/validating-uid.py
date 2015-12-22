"""
Problem Statement

ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each
of its employees.
The company has assigned you the task of validating all the randomly
generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise,
print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354: 1 is repeating --> Invalid
B1CDEF2354: Valid
"""
import re

invalid_pattern = "([A-Za-z0-9])\1*"
#pattern = "^([A-Za-z0-9])(?!\1*)[a-zA-Z0-9]{0,8}[a-zA-Z0-9]"
pattern = "^(?=[A-Z]{2, })(?=\d{3, }){10}$"
for _ in range(int(raw_input())):
    s = raw_input()
    if re.match(invalid_pattern, s):
        print "Invalid", re.match(invalid_pattern, s).groups()
    elif re.match(pattern, s):
        print "Valid"


