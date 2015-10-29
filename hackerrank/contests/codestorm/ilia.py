"""
Problem Statement

Ilia has N sticks. The size of the ith stick is Ai. He wants to know the number of different types of triangles created with each side from a single different stick. Help Ilia calculate the number of acute triangles, right triangles and obtuse triangles.

Input Format

The first line contains N.
The second line contains N integers. The ith number denotes Ai.

Constraints

For full score: 3?N?5000
For 40% score: 3?N?500
For all testcases:
1?A[i]?104
A[i]<A[i+1] where 1?i<N

Output Format

Print 3 integers: the number of acute triangles, right triangles and obtuse triangles, respectively.

Sample Input

6
2 3 9 10 12 15
Sample Output

2 1 4
Explanation

Acute triangles
10?12?15
9?10?12

Right triangle
9?12?15

Obtuse triangles
2?9?10
3?9?10
3?10?12
9?10?15
"""
import sys
from itertools import combinations
from math import sqrt

N = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
acute = 0
right = 0
obtuse = 0
for tup in list(combinations(A,  3)):
    a = tup[0]
    b = tup[1]
    c = tup[2]
    #print "".join(str(tup))
    if a+b <= c or b+c <= a or a+c <= b:
        continue
    if a**2 + b**2 > c**2 and b**2 + c ** 2 > a**2 and a**2 + c**2 > b**2:
        #print "ACUTE "+"".join(str(tup))
        acute += 1
    elif c == sqrt(a**2 + b**2) or a == sqrt(c**2 + b**2) or b == sqrt(a**2 + c**2):
        #print "RIGHT "+"".join(str(tup))
        right += 1
    elif (a**2 + b**2) < c**2 or (b**2 + c**2) < a**2 or (a**2 + c**2) < b**2:
        #print "OBTUSE "+"".join(str(tup))
        obtuse += 1
print acute, right, obtuse