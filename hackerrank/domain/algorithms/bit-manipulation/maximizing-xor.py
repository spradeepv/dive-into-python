"""
Given two integers, LL and RR, find the maximal value of AA xor BB, where AA
and BB satisfy the following condition:

L<=A<=B<=R
Input Format

The input contains two lines; L is present in the first line and R in the
second line.

Constraints
1<=L<=Rv101

Output Format

The maximal value as mentioned in the problem statement.

Sample Input

10
15
Sample Output

7
Explanation

The input tells us that L=10 and R=15. All the pairs which comply to
above condition are the following:
10XOR10=010XOR10=0
10XOR11=110XOR11=1
10XOR12=610XOR12=6
10XOR13=710XOR13=7
10XOR14=410XOR14=4
10XOR15=510XOR15=5
11XOR11=011XOR11=0
11XOR12=711XOR12=7
11XOR13=611XOR13=6
11XOR14=511XOR14=5
11XOR15=411XOR15=4
12XOR12=012XOR12=0
12XOR13=112XOR13=1
12XOR14=212XOR14=2
12XOR15=312XOR15=3
13XOR13=013XOR13=0
13XOR14=313XOR14=3
13XOR15=213XOR15=2
14XOR14=014XOR14=0
14XOR15=114XOR15=1
15XOR15=015XOR15=0
Here two pairs (10, 13) and (11, 12) have maximum xor value 7, and this is
the answer.
"""
def max_xor(l, r):
    max = -1
    for i in range(l, r+1):
        for j in range(i, r+1):
            x = i ^ j
            if x > max:
                max = x
    return max

l = int(raw_input())
r = int(raw_input())
print max_xor(l, r)