"""
Sansa has an array. She wants to find the value obtained by XOR-ing the
contiguous subarrays, followed by XOR-ing the values thus obtained. Can you
help her in this task?

Note : [5,7,5][5,7,5] is contiguous subarray of [4,5,7,5][4,5,7,5] while [4,
7,5][4,7,5] is not.

Input Format
First line contains an integer T, number of the test cases.
The first line of each test case contains an integer N, number of elements
in the array.
The second line of each test case contains NN integers that are elements of
the array.

Output Format
Print the answer corresponding to each test case in a separate line.

Constraints
1<=T<=5
2<=N<=10^5
1<=numbers in array<=10^8

Sample Input

2
3
1 2 3
4
4 5 7 5
Sample Output

2
0
Explanation

Test case #00:
1 XOR 2 XOR 3 XOR (1 XOR 2) XOR (2 XOR 3) XOR (1 XOR 2 XOR 3)=2
1 2 3 (1 3) (3 2) (1 3 2)

Test case #01:
4 XOR 5 XOR 7 XOR 5 XOR (4 XOR 5) XOR (5 XOR 7) XOR (7 XOR 5) XOR (4 XOR 5
XOR 7) XOR (5 XOR 7 XOR 5) XOR (4 XOR 5 XOR 7 XOR 5)=0

Editorial
---------
As we know "a XOR a" =0 So, When we write all substrings, We have to
check how many numbers are coming even number of time and how many numbers
coming odd number of times. So, If the list is 0 indexed. i.e. numbers are
indexed as "012.....N-1" Number at "ith" index will come "(i+1)*(N-i)"
number of times.

So, if "N" is even, either "i+1" or "N-i" will be even,
So each number will come even number of times. So, answer will be "0".
If "N" is odd, and "i" is even number, the give product will be
odd. So, answer will be XOR of even indexed numbers.
"""
for _ in range(int(raw_input())):
    n = int(raw_input())
    l = map(int, raw_input().split())
    if n % 2 == 0:
        print 0
    else:
        ans = 0
        for i in range(0, n + 1, 2):
            ans ^= l[i]
        print ans
