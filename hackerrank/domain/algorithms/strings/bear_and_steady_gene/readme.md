Bear and Steady Gene
--------------------

A gene is represented as a string of length n (where n is divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string s. It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of s and replace it with any substring of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string s, can you help Limak find the length of the smallest possible substring that he can replace to make ss a steady gene?

Note: A substring of a string S is a subsequence made up of zero or more consecutive characters of S.

Input Format
------------

The first line contains an interger n divisible by 4, denoting the length of a string s.

The second line contains a string s of length n. Each character is one of the four: A, C, T, G.

Constraints
-----------
4≤n≤500000
n is divisible by 4

Subtask
-------
4≤n≤2000 in tests worth 30% points.

Output Format
-------------

On a new line, print the minimum length of the substring replaced to make s stable.

Sample Input
------------

8

GAAATAAA

Sample Output
-------------

5

Explanation
-----------
One optimal solution is to replace a substring AAATA with TTCCG, resulting in GTTCCGAA. The replaced substring has length 5, so we print 5 on a new line.

Editorial
---------

Let's first think when Limak can choose some particular interval (substring). We should care about the remaining letters, both in the prefix and the suffix. If there are more than n/4 remaining letters of one type then we can't get a steady string. Otherwise, we know exactly how many letters of each type are missing and we can fill the removed interval with these exact letters. So, the interval can be chosen only if the remaining part doesn't contain more than n/4 letters of some type.

For each possible starting index of the interval let's find the nearest (leftmost) possible ending index. You can create four segment trees, one for each letter. Then, for fixed interval you can check in O(1) whether there are at most n/4 remaining letters of each type. So, for each starting index you can binary search the earliest good ending index. Segment trees and binary search give us O(nlog^2n). Let's make it faster.

First thing is to get rid of segment trees. It's enough to store prefix (and maybe suffix) sum for each letter, so you don't need segment trees anymore. It's ok to get AC but you can change one more thing. As we move with the starting index to the right, the ending index also moves to the right (or it doesn't change). So, we can use the two pointers technique to get O(n) solution. You can check codes below for details.
