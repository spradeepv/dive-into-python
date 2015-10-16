"""
Problem Statement

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number z Capture.PNG
z=x+yj
is completely determined by its real part x and imaginary part y.
j is the imaginary unit.

A polar coordinate (r,?) Capture.PNG

is completely determined by modulus r and phase angle ?.

If we convert complex number z to its polar coordinate, we find,
r : Distance from z to origin, i.e., x2+y2???????
? : Counter clockwise angle measured from the positive x-axis to the line segment that joins z to origin.

Python's cmath module provides acces to mathematical functions for complex numbers.

cmath.phase
Return phase of complex number z (also known as argument of z).

phase(complex(-1.0, 0.0))
3.1415926535897931
abs
Return modulus (absolute value) of complex number z.

abs(complex(-1.0, 0.0))
1.0
Task
You are given a complex z. Your task is to convert it to polar coordinate.

Input Format

Single line containing complex number z.

Output Format

Two lines:
First line contains, value of r.
Second line contains, value of ?.

Sample Input

  1+2j
Sample Output

 2.23606797749979
 1.1071487177940904

 Note : Output should be correct up to 3 decimal places.
"""

from cmath import phase

z_str = raw_input()
z_split = []
is_neg = False
if z_str.find("+") != -1:
    z_split = z_str.split("+")
elif z_str.find("-") != -1:
    z_split = z_str.split("-")
    is_neg = True
l = []
neg = False
index = 0
for i in z_split:
    if i.strip():
        if neg:
            l.append("-"+i)
            neg = False
        else:
            if is_neg and index > 0:
                l.append("-"+i)
            else:
                l.append(i)
    else:
        neg = True
    index += 1
x = float(l[0])
y = float(l[1][:-1])
#print x, y
print abs(complex(x, y))
print str(phase(complex(x, y)))