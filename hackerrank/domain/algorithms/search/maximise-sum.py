"""
Problem Statement

You are given an array of size N and another integer M. Your target is to
find the maximum value of sum of subarray modulo M.

Subarray is a continuous subset of array elements.

Note that we need to find the maximum value of (Sum of Subarray)%M ,
where there are N*(N+1)/2 possible subarrays.

Input Format
First line contains T , number of test cases to follow. Each test case
consists of exactly 2 lines. First line of each test case contain 2 space
separated integers N and M, size of the array and modulo value M.
Second line contains N space separated integers representing the elements of
the array.

Output Format
For every test case output the maximum value asked above in a newline.

Constraints
2 <= N <= 105
1 <= M <= 1014
1 <= elements of the array <= 1018
2 <= Sum of N over all test cases <= 500000

Sample Input

1
5 7
3 3 9 9 5
Sample Output

6
Explanation

Max Possible Sum taking Modulo 7 is 6 , and we can get 6 by adding first and
second element of the array
"""
import bisect

def max_mod(array, n, m):
    L = [0] * (n + 1)
    for i in range(1, n+1):
        L[i] = L[i - 1] + array[i - 1]
    #print L
    acc = 0
    done = []
    for i in range(n+1):
        x = L[i] % m
        j = bisect.bisect_right(done, x)
        acc = max(acc, x)
        # print done, (x, j), acc
        if j < i:
            acc = max(acc, (L[i] - done[j]) % m)
        done.insert(j, x)
    return acc


for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    b = [0] * (n + 1)
    l = map(long, raw_input().split())
    print max_mod(l, n, m)

