"""
Problem Statement

In the Quicksort challenges, you sorted an entire array. Sometimes, you just
need specific information about a list of numbers, and doing a full sort
would be unnecessary. Can you figure out a way to use your partition code to
find the median in an array?

Challenge
Given a list of numbers, can you find the median?

Input Format
There will be two lines of input:

n - the size of the array
ar - n numbers that makes up the array
Output Format
Output one integer, the median.

Constraints

1<=n<=1000001
n is odd
-10000<=x<=10000,x = ar
Sample Input

7
0 1 2 4 6 5 3
Sample Output

3
"""


def partition(ar, start, stop):
    pivot_index = stop - 1
    swap_index = start
    print start, stop, pivot_index
    for i in range(start, pivot_index):
        if ar[i] < ar[pivot_index]:
            ar[i], ar[swap_index] = ar[swap_index], ar[i]
            swap_index += 1

    ar[pivot_index], ar[swap_index] = ar[swap_index], ar[pivot_index]
    return swap_index


def find_median(ar, start, stop):
    median_index = len(ar) / 2
    while (True):
        pivot_index = partition(ar, start, stop)
        if pivot_index == median_index:
            return ar[pivot_index]
        elif pivot_index > median_index:
            stop = pivot_index
        else:
            start = pivot_index + 1
    return ar[pivot_index]


n = input()
ar = map(int, raw_input().strip().split(" "))
print find_median(ar, 0, len(ar))
