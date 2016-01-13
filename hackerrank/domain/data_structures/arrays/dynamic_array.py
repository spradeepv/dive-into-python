"""
Problem Statement

There are N sequences. All of them are initially empty, and you are given a
variable lastans=0. You are given Q queries of two different types:

"1 x y" - Insert y at the end of the ((x + lastans) mod N)th sequence.
"2 x y" - Print the value of the (y mod size)th element of the ((x + lastans)
mod N)th sequence. Here, size denotes the size of the related sequence.
Then, assign this integer to lastans.
Note: You may assume that, for the second type of query, the related
sequence will not be an empty sequence. Sequences and the elements of each
sequence are indexed by zero-based numbering.

The + symbol denotes the xor operation. You can get more information about
it from Wikipedia. It is defined as ^ in most of the modern programming
languages.

Input Format
-----------
The first line consists of N, number of sequences, and Q, number of queries,
separated by a space. The following Q lines contains one of the query types
described above.

Constraints
-----------
1<=N,Q<=105
0<=x<=109
0<=y<=109

Output Format
-------------
For each query of type two, print the answer on a new line.

Sample Input
-------------
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Sample Output
-------------
7
3

Explanation
------------
The first sequence is 5,3 and the second sequence is 7.
"""
n, q = map(int, raw_input().split())
lastans = 0
l = [[] for x in range(n)]
#print l
for _ in range(q):
    i, x, y = map(int, raw_input().split())
    if i == 1:
        #print (x ^ lastans) % n
        l[(x ^ lastans) % n].append(y)
    else:
        size = len(l[(x ^ lastans) % n])
        lastans = l[(x ^ lastans) % n][y % size]
        print lastans
