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
import numpy as np

def prefix_array(arr, n, m):
    curr = 0
    prefix = [0] * n
    for i in range(n):
        curr = (arr[i] % m + curr) % m
        prefix[i] = curr
    return prefix

for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    #print m
    l = map(long, raw_input().split())
    prefix = prefix_array(l, n, m)
    print prefix
