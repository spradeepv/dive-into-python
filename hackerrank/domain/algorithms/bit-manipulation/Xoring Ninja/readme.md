Xoring Ninja
------------

An XOR operation on a list is defined here as the xor (⊕) of all its elements (e.g.: XOR({A,B,C})=A⊕B⊕C).

The XorSum of set S is defined here as the sum of the XORs of all S's non-empty subsets. If we refer to the set of S's non-empty subsets as S′, this can be expressed as:

XorSum(S)=∑i=12n−1XOR(S′i)=XOR(S′1)+XOR(S′2)+⋯+XOR(S′2n−2)+XOR(S′2n−1)

For example: Given set S={n1,n2,n3}
The set of possible non-empty subsets is: S′={{n1},{n2},{n3},{n1,n2},{n1,n3},{n2,n3},{n1,n2,n3}}

The XorSum of these non-empty subsets is then calculated as follows:
XorSum(S) = n1+n2+n3+(n1⊕n2)+(n1⊕n3)+(n2⊕n3)+(n1⊕n2⊕n3)
Given a list of n space-separated integers, determine and print XorSum % (10^9+7)

Note: The cardinality of powerset(n)(n) is 2n2n, so the set of non-empty subsets of set S of size nn contains 2^n−1 subsets.

Input Format
------------
The first line contains an integer, TT, denoting the number of test cases.
Each test case consists of two lines; the first is an integer, nn, describing the size of the set, and the second contains nn space-separated integers (a1,a2,…,ana1,a2,…,an) describing the set.

Constraints
-----------
1≤T≤51≤T≤5
1≤n≤1051≤n≤105
0≤ai≤109, i∈[1,n]0≤ai≤109, i∈[1,n]

Output Format
-------------
For each test case, print its XorSum % (109+7)XorSum % (109+7) on a new line; the ithith line should contain the output for the ithith test case.

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
The input set, S={1,2,3}, has 7 possible non-empty subsets: S′={{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}}.

We then determine the XOR of each subset in S′:
XOR({1})=1
XOR({2})=2
XOR({3})=3
XOR({1,2})=1⊕2=3
XOR({2,3})=2⊕3=1
XOR({1,3}=1⊕3=2
XOR({1,2,3}=1⊕2⊕3=0

Then sum the results of the XOR of each individual subset in S′, resulting in XorSum=12. We print 12, because 12 % (10^9+7)=12.

