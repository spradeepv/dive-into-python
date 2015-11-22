#!/bin/python

from __future__ import division
import sys
from math import ceil, floor


N = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
mini = min(A)
s = 0
for i in A:
    s += i
r = (s/N)/N
B = [round(x/r) for x in A]
s = 0
for i in B:
    s += i
print int(s)