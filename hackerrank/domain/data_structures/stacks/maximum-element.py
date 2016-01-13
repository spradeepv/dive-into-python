"""
Problem Statement

You have an empty sequence, and you will be given N queries. Each query is
one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, N. The next N lines each
contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints
1<=N<=10^5
1<=x<=10^9
1<=type<=3
Output Format

For each type 3 query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
"""


class Stack(object):

    def __init__(self, n):
        self.stack_1 = [0 for x in range(n)]
        self.max_val_stack = [0 for x in range(n)]
        self.index_1 = -1
        self.index_2 = -1

    def push(self, val):
        if self.index_1 == -1:
            self.index_1 += 1
            self.index_2 += 1
            self.stack_1[self.index_1] = val
            self.max_val_stack[self.index_2] = val
        else:
            if val >= self.max_val_stack[self.index_2]:
                self.index_2 += 1
                self.max_val_stack[self.index_2] = val
            self.index_1 += 1
            self.stack_1[self.index_1] = val


    def pop(self):
        if self.stack_1[self.index_1] == self.max_val_stack[self.index_2]:
            self.index_2 -= 1
        self.index_1 -= 1

    def display(self):
        print self.max_val_stack[self.index_2]

n = int(raw_input())
stack = Stack(n)
for _ in range(n):
    l = map(int, raw_input().split())
    if len(l) == 1:
        if l[0] == 2:
            stack.pop()
        else:
            stack.display()
    else:
        val = l[1]
        stack.push(val)