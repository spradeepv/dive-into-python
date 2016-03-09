"""
You are given a set, S, of N distinct integers. Perform the operation
below on the set until such a point as the size of the set (|S|) no
longer changes when the operation is performed. The operation is as follows:

Choose any 2 distinct numbers, x and y, in set S. Calculate their
absolute difference (|x-y|), and insert the result into the set. Recall
that a set is a collection of distinct objects, so |S| will not change if
you attempt to insert a value it already contains.

Perform the above operation on S until until |S| no longer changes. Then
print the Mth greatest number present in the final set.

Note: It is guaranteed that |S|>=M.

Input Format

The first line contains an integer, N, denoting the size of the initial set.
The second line contains N space-separated integers denoting the elements
present in the initial set, S.
The third line contains an integer, M (our output is the Mth greatest
integer in the final set).

Constraints

2<=N<=10^5
1<=M<=10^5
All integers in initial set S are <=10^5
Output Format

Print the Mth greatest integer in the final set on a new line.

Sample Input

3
2 6 10
2
Sample Output

8
Explanation

Our initial set S=[2,6,10], and we will refer to the set resulting
from an operation as S'.

S=[2,6,10]. We choose x=2 and y=6. We insert |2-6|=4
into the set, resulting in S'=[2,4,6,10'].
S=[2,4,6,8]. We choose x=2 and y=10. We insert
|2-10|=8 into the set, resulting in S"=[2,4,6,8,10].
At this point, no operation using any possible x and y combination will
result in any new numbers being added to the set. Thus, our final set of
integers is [2,4,6,8,10].

M=2, and our Mth (2nd) greatest integer in [2,4,6,8,10] is 8, so we print 8
on a new line.

Editorial:
---------

Let the maximum integer in the initial set be PP and greatest common divisor
of all the integers in the initial array be GG.
Therefore, after applying all the possible operations, the final set will be
of the following form:
[1*G, 2*G, 3*G......, P]
[1*G, 2*G, 3*G......, P]
Hence, number of elements in the set will be equal to P / GP / G . Now,
you can easily find MMthth greatest integer as asked in the question.

On the side note, you might as well like to read Euclidean Theroem.
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


N = int(raw_input())
s = map(int, raw_input().split())
M = int(raw_input())
s.sort()
m = s[N - 1]
g = gcd(s[0], s[1])
for i in range(2, N - 1):
    g = gcd(g, s[i])
k = 1

#print g
if g == 1:
    s_ = [x for x in range(1, m+1)]
else:
    num = k * g
    s_ = set([x * g for x in range(m+1) if x*g <= m])
#print s_
s_ = sorted(s_, reverse=True)
#print s_
print s_[M - 1]
