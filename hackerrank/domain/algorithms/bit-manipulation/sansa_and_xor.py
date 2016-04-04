"""
Sansa has an array. She wants to find the value obtained by XOR-ing the
contiguous subarrays, followed by XOR-ing the values thus obtained. Can you
help her in this task?

Note : [5,7,5][5,7,5] is contiguous subarray of [4,5,7,5][4,5,7,5] while [4,
7,5][4,7,5] is not.

Input Format 
First line contains an integer TT, number of the test cases. 
The first line of each test case contains an integer NN, number of elements
in the array.
The second line of each test case contains NN integers that are elements of
the array.

Output Format 
Print the answer corresponding to each test case in a separate line.

Constraints 
1<=T<=5
2<=N<=105
1<=numbers in array<=108

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
1XOR2XOR3XOR(1XOR2)XOR(2XOR3)XOR(1XOR2XOR3)=21XOR2XOR3XOR(1XOR2)XOR(
2XOR3)XOR(1XOR2XOR3)=2

Test case #01: 
4XOR5XOR7XOR5XOR(4XOR5)XOR(5XOR7)XOR(7XOR5)XOR(4XOR5XOR7)XOR(5XOR7XOR5)XOR(
4XOR5XOR7XOR5)=0
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