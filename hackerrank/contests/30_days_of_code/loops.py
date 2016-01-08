"""
Problem Statement

Welcome to Day 5! Check out the video review of loops here, or just jump
right into the problem.

In this problem you will test your knowledge of loops. Given three integers
a, b, and N, output the following series:

a+2^0b,a+2^0b+2^1b....a+2^0b+2^1b+...+2^N-1b
Input Format

The first line will contain the number of testcases T. Each of the next T
lines will have three integers, a, b, and N.

Constraints

0<=T<=500
0<=a,b<=50
1<=N<=15
Output Format

Print the answer to each test case in a separate line.

Sample Input

2
5 3 5
0 2 10
Sample Output

8 14 26 50 98
2 6 14 30 62 126 254 510 1022 2046
Explanation

There are two test cases.
In the first case: a=5, b=3 ,N=5
1st term = 5+(2^0*3)=8
2nd term = 5+(2^0*3)+(2^1*3)=14
3rd term = 5+(2^0*3)+(2^1*3)+(2^2*3)=26
4th term = 5+(2^0*3)+(2^1*3)+(2^2*3)+(2^3*3)=50
5th term = 5+(2^0*3)+(2^1*3)+(2^2*3)+(2^3*3)+(2^4*3)=98
"""
for _ in range(int(raw_input())):
    a, b, N = map(int, raw_input().split())
    series = 0
    for i in range(N):
        series = a
        for j in range(i+1):
            series += (pow(2, j) * b)
        print series,
    print