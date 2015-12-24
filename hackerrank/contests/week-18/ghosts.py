#!/bin/python

import sys
from itertools import product
from fractions import gcd

A,B,C,D = raw_input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]
a = [x for x in range(1, A + 1)]
b = [x for x in range(1, B + 1)]
c = [x for x in range(1, C + 1)]
d = [x for x in range(1, D + 1)]
l = [a, b, c, d]
count = 0
for tup in list(product(*l)):
    A = tup[0]
    B = tup[1]
    C = tup[2]
    D = tup[3]
    if abs(A-B) % 3 == 0 and (B + C) % 5 == 0 and (A * C) % 4 == 0 and \
                    gcd(A, D) == 1:
        count += 1
print count
