"""
Problem Statement

Sherlock is given an array of N integers (A0, A1 ... AN-1 by Watson. Now
Watson asks Sherlock how many different pairs of indices i and j exist such
that i is not equal to i but Ai is equal to Ai.

Input Format
The first line contains T, the number of test cases. T test cases follow.
Each test case consists of two lines; the first line contains an integer N,
the size of array, while the next line contains N space separated integers.

Output Format
For each test case, print the required answer on a different line.

Constraints
1<=T<=10
1<=N<=105
1<=A[i]<=106

Sample input

2
3
1 2 3
3
1 1 2
Sample output

0
2
Explanation
In the first test case, no two pair of indices exist which satisfy the given
condition.
In the second test case as A[0] = A[1] = 1, the pairs of indices (0,1) and (
1,0) satisfy the given condition.
"""
for _ in range(int(raw_input())):
    n = int(raw_input())
    l = map(int, raw_input().split())
    dict = {}
    for i in range(n):
        num = l[i]
        if dict.has_key(num):
            dict.get(num).append(i)
        else:
            dict[num] = [i]
    #print dict
    found = False
    count = 0
    for k, v in dict.items():
        if v and len(v) > 1:
            count += len(v) * (len(v) - 1)
            found = True
    if found:
        print count
    else:
        print 0