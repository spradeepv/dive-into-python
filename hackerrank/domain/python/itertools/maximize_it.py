"""
Problem Statement

You are given a function f(X)=X2.

You are also given K lists. The ith list consists of Ni elements.

You have to pick exactly one element from each list such that S=(f(X1)+f(X2)+...+f(Xk))%M is  maximized. Xi denotes the element picked from the ith list . Find the maximized value Smax thus obtained.

% denotes the modulo operator.

Input Format
First line contains 2 space seperated integers K and M.
Then follow K lines.
The (i+1)th line contains an integer Ni followed by Ni space seperated integers denoting the elements in the list.

Output Format
A single integer denoting the value Smax.

Constraints
1?K?7
1?M?1000
1?Ni?7
1?Magnitudeofelementsinlist?109

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output

206
Explanation

Picking 5 from the 1st list , 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (52+92+102)%1000 = 206.
"""
from itertools import product

k, m = map(int, raw_input().split())
l = []
for i in range(k):
    l.append(raw_input().split()[1:])
li = []
for i in range(k):
    for j in range(i+1, k):
        li = list(product(*l))
sum = 0
print li
for tup in li:
    total = 0
    for i in tup:
        i = int(i) ** 2
        total += i
    total = total % m
    if total > sum:
        sum = total
print sum