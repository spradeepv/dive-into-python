"""
An XOR operation on a list is defined here as the xor (XOR) of all its
elements (e.g.: XOR({A,B,C})=A XOR B XOR C).

The XorSum of set S is defined here as the sum of the XORs of all
S's non-empty subsets. If we refer to the set of S's non-empty subsets as
S'.

For example: Given set S={n1,n2,n3}
The set of possible non-empty subsets is: S'={{n1},{n2},{n3},{n1,n2},{n1,
n3},{n2,n3},{n1,n2,n3}}

The XorSum of these non-empty subsets is then calculated as follows:
XorSum(S) = n1+n2+n3+(n1 XOR n2)+(n1 XOR n3)+(n2 XOR n3)+(
n1 XOR n2 XOR n3)
Given a list of n space-separated integers, determine and print XorSum % (
10^9+7).

Note: The cardinality of powerset(n)is 2^n, so the set of non-empty
subsets of set S of size n contains 2^(n-1) subsets.

Input Format
------------
The first line contains an integer, T, denoting the number of test cases.
Each test case consists of two lines; the first is an integer, n,
describing the size of the set, and the second contains nn space-separated
integers (a1,a2,...,an) describing the set.

Constraints
-----------
1<=T<=5
1<=n<=10^5
0<=ai<=10^9, i==[1,n]

Output Format
-------------
For each test case, print its XorSum % (10^9+7) on a new
line; the ith line should contain the output for the ith test case.

Sample Input
------------
1
3
1 2 3

Sample Output
-------------
12

Explanation
-----------
The input set, S={1,2,3}S={1,2,3}, has 77 possible non-empty subsets: S'={{
1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}}.

We then determine the XORXOR of each subset in S':
XOR({1})=1XOR({1})=1 
XOR({2})=2XOR({2})=2 
XOR({3})=3XOR({3})=3 
XOR({1,2})=1XOR2=3
XOR({2,3})=2XOR3=1
XOR({1,3}=1XOR3=2
XOR({1,2,3}=1XOR2XOR3=0

Then sum the results of the XOR of each individual subset in S',
resulting in XorSum=12. We print 1212, because 12 % (10^9+7)=12 %
(10^9+7)=12.

Editorial
---------
Solution: Find OR of all the elements and multiply it with 2^(n-1) where n
is the total number of elements. This gives us the answer.
Idea:
There will be total 2^n subsets.
If ith bit of any element is set, then that bit will be set in xor of half
of the total subsets which is 2^(n-1).
To find out all the set bits in all the numbers we find OR of all the numbers.
Since each set bit appears in half of the total subsets we multiply OR of
all numbers with 2^n-1 to get the final result.
"""
for _ in range(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    answer = a[0]
    for i in range(1, n):
        answer |= a[i]
    print (answer * pow(2, n-1)) % (pow(10, 9) + 7)