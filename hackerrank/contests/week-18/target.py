#!/bin/python

import sys
from math import sqrt

K, N = raw_input().strip().split(' ')
K, N = [int(K), int(N)]
R = map(int, raw_input().strip().split(' '))
x = []
score = 0
for x_i in xrange(N):
    x_temp = map(int, raw_input().strip().split(' '))
    if x_temp[0] == 0 and x_temp[1] == 0:
        #print K
        score += K
    elif x_temp[0] == 0 or x_temp[1] == 0:
        matches = [x for x in R if x <= max(x_temp[0], x_temp[1])]
        point = 0
        if matches:
            if matches[0] == max(x_temp[0], x_temp[1]):
                point = R.index(matches[0]) + 1
            elif matches[0] < max(x_temp[0], x_temp[1]):
                point = R.index(matches[0])
        else:
            point = K
        #print point
        score += point
    else:
        radius = sqrt(x_temp[0] ** 2 + x_temp[1] ** 2)
        #print radius
        matches = [x for x in R if x <= radius]
        point = 0
        #print matches
        if matches:
            if matches[0] == radius:
                point = R.index(matches[0]) + 1
            elif matches[0] < radius:
                point = R.index(matches[0])
        else:
            point = K
        #print point
        score += point
print score

