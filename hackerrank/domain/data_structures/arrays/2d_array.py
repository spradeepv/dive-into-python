"""
Problem Statement

You are given a 6*6 2D array. An hourglass in an array is a portion shaped like this:

a b c
  d
e f g
For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Actually there are many hourglasses in the array above. The three leftmost hourglasses are the following:

1 1 1     1 1 0     1 0 0
  1         0         0
1 1 1     1 1 0     1 0 0
The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.

In this problem you have to print the largest sum among all the hourglasses in the array.

Note: If you have already solved the problem Java 2D array in the data structures chapter in the Java domain, you may skip this challenge.

Input Format

There will be exactly 6 lines, each containing 6 integers seperated by spaces. Each integer will be between -9 and 9 inclusive.

Output Format

Print the answer to this problem on a single line.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19

Explanation

The hourglass which has the largest sum is:

2 4 4
  2
1 2 4
"""

l = [[0 for x in range(6)] for x in range(6)]

for i in range(6):
    li = map(int, raw_input().split())
    for j in range(6):
        l[i][j] = li[j]
print ">>>>", l[5][2]
for i in range(0, 4):
    for j in range(i, i+3):
        for m in range(0, 3):
            for k in range(m, m+3):
                print l[j][k],
            print
    print
    # for j in range(i, i+3):
    #     for k in range(1, 4):
    #         print l[j][k],
    #     print
    # print