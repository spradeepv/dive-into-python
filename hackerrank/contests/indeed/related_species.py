"""
Problem Statement

A group of scientists have broken down species DNA into sequences of integers. They determine that two species with the respective DNA sequences A and B are considered to be related if a non-decreasing sequence C of the same length can be found, such that Ci=Ai or Ci=Bi.

Given the DNA sequences for two species, help the scientists determine if they are related.

Input Format

The first line contains an integer, T, the number of test cases.

For each test case:
The first line contains an integer, N, the length of the DNA sequence.
The second line contains a sequence of space-separated integers describing species A.
The third line contains a sequence of space-separated integers describing species B.

Constraints:
1?T?5
1?N?105
0?Ai, Bi?1010
Output Format

On a new line for each test case, print YES if a non-decreasing sequence of the same length can be found (i.e.: species are related) or NO if it cannot.

Sample Input

3
3
1 2 3
4 4 4
3
3 2 1
6 5 4
2
1 0
10 2
Sample Output

YES
NO
YES
Explanation

Test Case 1: We could have C=1 2 4
Test Case 2: No increasing sequence C is possible.
Test Case 3: We could have C=1 2.
"""

for _ in range(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    last = -1
    related = True
    for i in range(n):
        #print last, a[i], b[i]
        if a[i] < b[i] and a[i] > last:
            last = a[i]
            continue
        elif b[i] < a[i] and b[i] > last:
            last = b[i]
            continue
        elif a[i] > b[i] and a[i] > last:
            last = a[i]
            continue
        elif b[i] > a[i] and b[i] > last:
            last = b[i]
            continue
        else:
            related = False
    print "YES" if related else "NO"