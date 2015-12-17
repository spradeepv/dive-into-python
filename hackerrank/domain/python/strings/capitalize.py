"""
Problem Statement

You are given a string S. Your task is to capitalize each word of S.

Input Format

A single line of input containing the string, S.

Constraints

0<len(S)<1000
The string consists of alphanumeric characters and spaces.

Output Format

Print the capitalized string, S.

Sample Input

hello world
Sample Output

Hello World
"""

s = raw_input()
l = []
for i in s.split(" "):
    l.append(i.capitalize())
print " ".join(l)