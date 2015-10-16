# -*- coding: utf-8 -*-
"""
ABC is a right angle triangle, right angled at B.
Therefore, ABC=90 degree.

Point M is the mid-point of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find ∡MBC ( angle θ degree, as shown in figure ) in degrees.

Input Format

First line contains, length of side AB.
Second line contains, length of side BC.

Constraints

0<AB<100
0<BC<100
Lengths AB and BC are natural numbers.

Output Format

Output ∡MBC in degrees.

Note: Round-off the angle to nearest integer.
Examples:
If angle is 56.5000001, then output 57.
If angle is 56.5000000, then output 57.
If angle is 56.4999999, then output 56.

0<θ<90
Sample Input

10
10
Sample Output

45
NOTE : Python 3 is disabled for this challenge.
"""
import math

def find_angle(bc, ac, ab):
    t = (bc ** 2 + ac ** 2 - ab ** 2)/(2 * (bc * ac))
    print math.degrees(math.acos(t))
    return round(math.degrees(math.acos(t)))

ab = int(raw_input())
bc = int(raw_input())
ac = math.hypot(ab, bc)/2
print ab, bc, ac
M = round(math.acos((ac ** 2 + bc ** 2 - ac ** 2)/(2 * ac * bc) )* 180/math.pi)
print str(int(M)) + "°"