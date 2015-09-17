"""
Task

Apply your knowledge of .add() operation, to help your friend 'Hari'.

Hari has a huge collection of country stamps. He decided to count total number of distinct country stamps he has collected. He asked you to help him. You pick stamps one by one from a stack of 'N' country stamps.

Your task is to find the total number of distinct country stamps.

Input Format

First line contains N, total number of country stamps.
Next N lines contains, names of the country stamp.
Constraints

0<N<1000
Output Format

Output the total number of distinct country stamps.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France
Sample Output

5
Explanation

UK and France are repeating twice. Hence, total number of distinct country stamps is 5 (five).
"""
n = int(raw_input())
s = set()
for i in range(n):
    s.add(raw_input().strip())
print len(s)