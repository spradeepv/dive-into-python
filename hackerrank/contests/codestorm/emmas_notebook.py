"""
Problem Statement

Emma is writing bits (1s and 0s) in her notebook. Every second, she writes some
more bits.

In the 1st second, she writes two bits in her notebook. She starts with 0 and
alternates between 0 and 1. They look like this:
0 1
In the 2nd second, she writes three more bits in her notebook. This time, she
starts with 1 and keeps alternating between 0 and 1. Now, they look like this:
0 1
1 0 1
After 6 seconds, her notebook looks like this:
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
1 0 1 0 1 0 1
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0 1
If you count carefully, you can see that Emma wrote 15 1's in her notebook
after 6 seconds. She wants to know how many 1's she can write in t seconds.

Input Format:
-------------
Input contains just one integer: t.
Constraints
1<=t<=105
Output Format
-------------
Print the number of 1's Emma can write in t seconds.

Sample Input 1
--------------
3
Sample Output 1
---------------
5
Explanation 1 Add one more row to the example of the 2nd second above and
then you will see five 1's in total.

Sample Input 2
--------------
6
Sample Output 2
---------------
15
Explanation 2 See the example after 6 seconds above.
"""
t = int(raw_input())
result = 1
for i in range(t, 1, -1):
    result += (i/2 + 1)
print result