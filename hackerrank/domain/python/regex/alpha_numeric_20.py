"""
Alphanumeric and length 20 chars
"""
import re

s = raw_input()
print s
#pattern = r"^[a-zA-Z]{5, 20}$"
pattern = r"^[\w]{3,20}$"
if re.match(pattern, s):
    print "Matches"
else:
    print "Error"
