"""
Jigar got a sequence of n positive integers as his birthday present! He
likes consecutive subsequences whose sum is divisible by k. He asks you to
write a program to count them for him.

Input Format
The first line contains T, the number of testcases.
T testcases follow. Each testcase consists of 2 lines.
The first line contains n and k separated by a single space.
And the second line contains n space separated integers.

Output Format
For each test case, output the number of consecutive subsequenences whose
sum is divisible by k in a newline.

Constraints
1 <= T <= 20
1 <= n <= 106
1 <= k <= 100
1 <= a[i] <= 104

Sample Input

2
5 3
1 2 3 4 1
6 2
1 2 1 2 1 2
Sample Output

4
9
Explanation

For

1 2 3 4 1
there exists, 4 subsequences whose sum is divisible by 3, they are

3
1 2
1 2 3
2 3 4
For

1 2 1 2 1 2
there exists, 9 subsequences whose sum is divisible by 2, they are

2
2
2
1 2 1
1 2 1
1 2 1 2
2 1 2 1
1 2 1 2
2 1 2 1 2
"""


def kSub(k, nums):
    l = [0 for x in range(100)]
    sum = 0
    l[0] = 1
    for num in nums:
        sum += num
        if sum >= k:
            sum %= k
        l[sum] += 1
        print num, sum
    print l
    ret = 0
    for i in range(k):
        ret += l[i] * (l[i] - 1) / 2
        print ret
    return ret

def sub_seq(k, nums):
    l = [0 for x in range(100)]
    sum1 = [0] * len(nums)
    l[0] = 1
    for i in range(len(nums)):
        sum1[i] = (sum1[i-1] + nums[i])%k
        l[sum1[i]] += 1
        print i, sum1[i]
        print l
    print l
    ret = 0
    for i in range(k):
        ret += l[i] * (l[i] - 1) / 2
        print ret
    return ret

for _ in range(int(raw_input())):
    n, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    print kSub(k, l)
