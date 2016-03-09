"""
Watson gives Sherlock an array A1,A2...AN.
He asks him to find an integer M between P and Q(both inclusive), such that,
min {|Ai-M|, 1 <= i <= N} is maximised. If there are multiple solutions,
print the smallest one.

Input Format
The first line contains N. The next line contains space separated N
integers, and denote the array A. The third line contains two space
separated integers denoting P and Q.

Output Format
In one line, print the required answer.

Constraints
1 <= N <= 102
1 <= Ai <= 109
1 <= P <= Q <= 109

Sample Input

3
5 8 14
4 9
Sample Output

4
Explanation
For M = 4,6,7, or 9, the result is 1. Since we have to output the smallest
of the multiple solutions, we print 4.
"""
def mini_(arr, n, x):
    #print arr, n, x
    low = mid = 0
    high = n-1
    while low <= high:
        mid = (low+high)/2
        print mid, x
        if arr[mid] == x:
            return 0
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    if low == 0 or abs(arr[low] - x) < abs(arr[low-1] - x):
        return abs(arr[low] - x)
    else:
        return abs(arr[low-1] - x)

n = int(raw_input())
a = map(int, raw_input().split())
p, q = map(int, raw_input().split())
range_ = [x for x in range(p, q+1)]
min_list = []
for x in range(p, q+1):
    mini = 1000000000
    for i in a:
        mini = min(mini, abs(i - x))
    min_list.append(mini)
max = max(min_list)
#print range_[min_list.index(max)]
ans = -1
a.sort()
l = 0
for x in range(p, q+1):
    m = mini_(a, n, x)
    if ans < m:
        ans = m
        l = x
print l
