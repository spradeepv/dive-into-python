"""
Problem Statement

You are given an integer N. Print the factorial of this number.

N!=Nx(N?1)x(N?2)x?x3x2x1
Note: Factorials of N>20 can't be stored even in a 64?bit long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers but we need to write additional code in C/C++ to handle such large values.

We recommend solving this challenge using BigIntegers.

Input Format
Input consists of a single integer N.

Constraints
1?N?100

Output Format
Output the factorial of N.

Sample Input

25
Sample Output

15511210043330985984000000
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(raw_input())
print factorial(n)

