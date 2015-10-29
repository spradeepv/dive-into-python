"""
Problem Statement

In Quantumland, there are n cities numbered from 1 to n. Here, ci denotes the ith city. There are n?1 roads in Quantumland. Here, ci and ci+1 have a bidirectional road between them for each i<n.

There is a rumor that Flatland is going to attack Quantumland, and the queen wants to keep her land safe. The road between ci and ci+1 is safe if there is a guard in ci or ci+1.

The queen has already placed a few guards in some of the cities, but she is not sure if they are enough to keep the roads safe. She wants to know the minimum number of new guards she needs to hire.

Input Format

The first line will contain an integer t: denoting the number of testcases.

For each testcase, there will be 2 lines.

The first line will contain an integer n.
In the next line, there will be n integers b1,b2...bn.

If bi=1, that means there is a guard in city ci.
If bi=0, that means there are no guards in city ci.

Constraints

1<=t<=1000
1<=n<=100
Output Format

Print the minimum number of new guards that need to be hired to make Quantumland safe.

Sample Input

2
5
1 1 0 1 0
5
0 0 1 0 0
Sample Output 1

0
2
The following figure represents the first testcase. The cities with guards are marked in blue.

cover(1).png

All the roads are safe. No more guards are needed. The output is 0.

The next figure represents the second testcase. The old guards are marked in blue, and the new guards are marked in yellow.

cover3.png

Note: There can be more than one way to make Quantumland safe using the minimum number of new guards. In the second testcase, we could also place new guards in city 1 and city 4 instead of city 2 and city 4.
"""
#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    safe = False
    result = 0
    for i in range(0, len(a)):
        if a[i] == 0 and (i + 1) < len(a) and a[i+1] == 0:
            result += 1
            a[i+1] = 1
    print result