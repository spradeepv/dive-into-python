"""
Task

Your are given a two lists A and B. Your task is to compute Cartesian Product AXB.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note : A and B are sorted lists and the cartesian product's tuples should be emitted in sorted order.

Input Format

First line contains, space separated elements of list A.
Second line contains, space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints

0<A<30
0<B<30
Output Format

Output space separated tuples of Cartesian Product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
"""
from itertools import product

a = map(int, raw_input().split())
b = map(int, raw_input().split())
print " ".join("(%s, %s)" % tup for tup in list(product(a, b)))
