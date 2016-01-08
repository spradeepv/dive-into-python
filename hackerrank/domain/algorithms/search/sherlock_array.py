"""
Watson gives Sherlock an array A of length N. Then he asks him to determine
if there exists an element in the array such that the sum of the elements on
its left is equal to the sum of the elements on its right. If there are no
elements to the left/right, then the sum is considered to be zero.
Formally, find an i, such that, A1+A2...Ai-1 =Ai+1+Ai+2...AN.

Input Format
The first line contains T, the number of test cases. For each test case,
the first line contains N, the number of elements in the array A. The second
line for each test case contains N space-separated integers, denoting the
array A.

Output Format
For each test case print YES if there exists an element in the array,
such that the sum of the elements on its left is equal to the sum of the
elements on its right; otherwise print NO.

Constraints
1<=T<=10
1<=N<=105
1<=Ai <=2*104
1<=i<=N
Sample Input

2
3
1 2 3
4
1 2 3 3
Sample Output

NO
YES
Explanation
For the first test case, no such index exists.
For the second test case, A[1]+A[2]=A[4], therefore index 3 satisfies the
given conditions.
"""
def is_sherlock_array(arr):
    length = len(arr)
    if length == 1:
        return True
    is_sherlock_array = False
    curr = 0
    left_sum = arr[0] + curr
    right_sum = sum(arr[2:length])
    for i in range(1, length-1):
        #print left_sum, right_sum
        if left_sum == right_sum:
            is_sherlock_array = True
        prev = arr[i]
        curr = arr[i+1]
        left_sum += prev
        right_sum -= curr
    return is_sherlock_array


def get_input():
    test_cases = int(raw_input())
    for i in range(test_cases):
        n = int(raw_input())
        arr = map(int, raw_input().split())
        # print arr
        print "YES" if is_sherlock_array(arr) else "NO"

get_input()
