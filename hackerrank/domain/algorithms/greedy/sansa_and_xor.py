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
1 XOR 2 XOR 3 XOR (1 XOR 2) XOR (2 XOR 3) XOR (1 XOR 2 XOR 3)=21 XOR 2 XOR 3
XOR (1 XOR 2) XOR (2 XOR 3) XOR (1 XOR 2 XOR 3)=2

Test case #01:
4 XOR 5 XOR 7 XOR 5 XOR (4 XOR 5) XOR (5 XOR 7) XOR (7 XOR 5) XOR (4 XOR 5
XOR 7) XOR (5 XOR 7 XOR 5) XOR (4 XOR 5 XOR 7 XOR 5)=0
"""

def get_sub_array(lst   ):
    result = []
    start = 0
    while start < len(lst):
        try:
            end = lst.index(item, start + 1)
        except ValueError:
            end = len(lst)
        result.extend(lst[x+start:x+start+size] for x in range(end - start - size + 1))
        start = end + 1

for _ in range(int(raw_input())):
    n = int(raw_input())
    l = map(int, raw_input().split())

