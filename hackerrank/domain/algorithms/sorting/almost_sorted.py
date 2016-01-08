"""
Problem Statement

Given an array with n elements, can you sort this array in ascending order
using only one of the following operations?

Swap two elements.
Reverse one sub-segment.
Input Format
The first line contains a single integer, n, which indicates the size of the
array.
The next line contains n integers separated by spaces.

n
d1 d2 ... dn
Constraints
2<=n<=100000
0<=di<=1000000
All di are distinct.

Output Format
1. If the array is already sorted, output yes on the first line. You do not
need to output anything else.

If you can sort this array using one single operation (from the two
permitted operations) then output yes on the first line and then:

a. If you can sort the array by swapping dl and dr, output swap l r in the
second line. l and r are the indices of the elements to be swapped, assuming
that the array is indexed from 1 to n.

b. Else if it is possible to sort the array by reversing the segment d[
l...r], output reverse l r in the second line. l and r are the indices of
the first and last elements of the subsequence to be reversed, assuming that
the array is indexed from 1 to n.

d[l...r] represents the sub-sequence of the array, beginning at index l and
ending at index r, both inclusive.

If an array can be sorted by either swapping or reversing, stick to the
swap-based method.

If you cannot sort the array in either of the above ways, output no in the
first line.

Sample Input #1

2
4 2
Sample Output #1

yes
swap 1 2
Sample Input #2

3
3 1 2
Sample Output #2

no
Sample Input #3

6
1 5 4 3 2 6
Sample Output #3

yes
reverse 2 5
Explanation
For #1, you can both swap(1, 2) and reverse(1, 2), but if you can sort the
array using swap, output swap only.
For #2, it is impossible to sort by one single operation (among those
permitted).
For #3, you can reverse the sub-array d[2...5] = "5 4 3 2", then the array
becomes sorted.
"""
n = int(raw_input())
ar = map(int, raw_input().split())


def is_sorted(ar):
    for i in xrange(1, len(ar)):
        if ar[i-1] > ar[i]:
            return False
    return True


def almost_sorted(ar):
    index_mismatch = []
    for i in xrange(1, n):
        if ar[i] < ar[i-1]:
            index_mismatch.append(i)
    print index_mismatch
    if not index_mismatch:
        print 'yes'
        return
    elif len(index_mismatch) == 1:
        i, j = index_mismatch[0]-1, index_mismatch[0]
        ar[i], ar[j] = ar[j], ar[i]
        if is_sorted(ar):
            print 'yes'
            print 'swap', index_mismatch[0], index_mismatch[0]+1
            return
    elif len(index_mismatch) == 2:
        for i in [index_mismatch[0]-1, index_mismatch[0]]:
            for j in [index_mismatch[1]-1, index_mismatch[1]]:
                #print i, j
                if i != j:
                    ar[i], ar[j] = ar[j], ar[i]
                    if is_sorted(ar):
                        a, b = sorted([i+1, j+1])
                        print 'yes'
                        print 'swap', a, b
                        return
                    ar[i], ar[j] = ar[j], ar[i]
    elif index_mismatch[-1] - index_mismatch[0] == len(index_mismatch) - 1:
        l, r = index_mismatch[0]-1, index_mismatch[-1]+1
        ar[l:r] = reversed(ar[l:r])
        if is_sorted(ar):
            print 'yes'
            print 'reverse', l+1, r
            return
    print 'no'
almost_sorted(ar)

