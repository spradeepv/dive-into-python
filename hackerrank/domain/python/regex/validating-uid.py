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

#match_upper_case = r"([A-Z].*?)"

invalid_pattern = r"([a-zA-Z0-9])[a-zA-Z0-9]*\1"
upper_case_match = r"([A-Z].*?)"
digit_pattern = r"([0-9].*?)"
length_pattern = r"([A-Za-z0-9]){10}"
for _ in range(int(raw_input())):
    s = raw_input()
    invalid_match = re.search(invalid_pattern, s)
    length_match = re.match(length_pattern, s)
    if invalid_match or not length_match:
        print "Invalid"
        continue
    match_upper_case = re.findall(upper_case_match, s)
    match_digit = re.findall(digit_pattern, s)
    print len(match_upper_case), len(match_digit), length_match
    if length_match and len(match_upper_case) >= 2 and len(match_digit) >= 3:
        print "Valid"
    else:
        print "Invalid"