"""
Problem Statement

Bob is in a candy shop and wants to purchase his favorite candy, which he knows costs N dollars. He has an infinite number of 1,2,5,10,20,50, and 100 dollar bills in his pocket. Bob wants to know the number of different ways he can pay the N dollars for his candy.

Input Format

A single integer, N, which is the cost of Bob's candy.

Constraint
1?N?250

Output Format

Print an integer representing the number of different variations of how Bob can pay.

Sample Input1

5
Sample Output1

4
Sample Input2

7
Sample Output2

6
Explanation

Sample 1: 4 variants

(1,1,1,1,1)
(2,1,1,1)
(2,2,1)
(5)
Sample 2: 6 variants

(1,1,1,1,1,1,1)
(2,1,1,1,1,1)
(2,2,1,1,1)
(2,2,2,1)
(5,1,1)
(5,2)
"""
def subset_sum(number, l):
    ways = [0] * (number + 1)
    ways[0] = 1
    for n in l:
        for j in xrange(n, number + 1):
            ways[j] += ways[j - n]
    return ways[number]

n = int(raw_input())
print subset_sum(n, [1, 2, 5, 10, 20, 50, 100])
