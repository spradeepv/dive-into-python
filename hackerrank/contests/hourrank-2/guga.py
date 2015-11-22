import sys
import re

N = int(raw_input().strip())
s = 0
for i in range(5, (2**N)+1):
    b = bin(i)[2:]
    print i, b
    b = '101101'
    pattern = "10+?1"
    print re.findall(pattern, b)
    s += len(re.findall(pattern, b))

print s