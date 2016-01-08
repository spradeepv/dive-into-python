"""
Problem Statement

Insertion Sort is a simple sorting technique which was covered in previous
challenges. Sometimes, arrays may be too large for us to wait around for
insertion sort to finish. Is there some other way we can calculate the
number of times Insertion Sort shifts each elements when sorting an array?

If ki is the number of elements over which the ith element of the array has
to shift, then the total number of shifts will be k1 +k2 +...+kN.

Input Format
The first line contains the number of test cases, T. T test cases follow.
The first line for each test case contains N, the number of elements to be
sorted. The next line contains N integers (a[1], a[2], ..., a[N]).

Output Format
Output T lines containing the required answer for each test case.

Constraints
1<=T<=15
1<=N<=100000
1<=a[i]<=10000000
Sample Input

2
5
1 1 1 2 2
5
2 1 3 1 2
Sample Output

0
4
Explanation
The first test case is already sorted, therefore there's no need to shift
any element. In the second case, it will proceed in the following way.

Array: 2 1 3 1 2 -> 1 2 3 1 2 -> 1 1 2 3 2 -> 1 1 2 2 3
Moves:   -        1       -    2         -  1            = 4
"""
def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    print lst
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    print a, b, c, result
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

for _ in range(int(raw_input())):
    n = int(raw_input())
    ar = map(int, raw_input().split())
    print count_inversion(ar)
