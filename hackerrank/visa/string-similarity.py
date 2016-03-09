"""
For two strings A and B, we define the similarity of the strings to be the
length of the longest prefix common to both strings. For example,
the similarity of strings "abc" and "abd" is 2, while the similarity of
strings "aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

Input:
The first line contains the number of test cases T. Each of the next T lines
contains a string each.

Output:
Output T lines containing the answer for the corresponding test case.

Constraints:
1 <= T <= 10
The length of each string is at most 100000 and contains only lower case
characters.

Sample Input:

2
ababaa
aa
Sample Output:

11
3
Explanation:
For the first case, the suffixes of the string are "ababaa", "babaa",
"abaa", "baa", "aa" and "a". The similarities of these strings with the
string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is 6 + 0 +
3 + 0 + 1 + 1 = 11.

For the second case, the answer is 2 + 1 = 3.
"""
def stringSimilarity(inputs):
    ret = []
    for a in inputs:
        n = len(a)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if (i <= r):
                z[i] = min(r - i + 1, z[i - l])
            while (i + z[i] < n and a[z[i]] == a[i + z[i]]):
                z[i] += 1
            if (i + z[i] - 1 > r):
                l = i
                r = i + z[i] - 1
        ret.append(sum(z) + n)
    return ret


inputs = []
for _ in range(int(raw_input())):
    inputs.append(raw_input())

for i in stringSimilarity(inputs):
    print i
