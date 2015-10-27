"""
Problem Statement

An array is a series of elements of the same type placed in contiguous memory locations that can be individually referenced by adding an index to a unique identifier.

You'll be an given array of N integers and you have to print the integers in the reverse order.

Note: If you have already solved the problem Arrays Introduction in the Introduction chapter in C++ domain, you may skip this challenge.

Input Format

The first line of the input contains N,where N is the number of integers.The next line contains N integers separated by a space.

Constraints

1<=N<=1000
1<=Ai<=10000, where Ai is the ith integer in the array.

Output Format

Print the N integers of the array in the reverse order in a single line separated by a space.

Sample Input

4
1 4 3 2
Sample Output

2 3 4 1
"""
n = int(raw_input())
l = map(int, (raw_input().split()))
for i in range(n-1, -1, -1):
    print l[i],

