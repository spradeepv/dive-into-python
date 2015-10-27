"""
Problem Statement

Sherlock Holmes is getting paranoid about Professor Moriarty, his arch-enemy. All his efforts to subdue Moriarty have been in vain. These days Sherlock is working on a problem with Dr. Watson. Watson mentioned that the CIA has been facing weird problems with their supercomputer, 'The Beast', recently.

This afternoon, Sherlock received a note from Moriarty, saying that he has infected 'The Beast' with a virus. Moreover, the note had the number N printed on it. After doing some calculations, Sherlock figured out that the key to remove the virus is the largest Decent Number having N digits.

A Decent Number has the following properties:

3, 5, or both as its digits. No other digit is allowed.
Number of times 3 appears is divisible by 5.
Number of times 5 appears is divisible by 3.
Meanwhile, the counter to the destruction of 'The Beast' is running very fast. Can you save 'The Beast', and find the key before Sherlock?

Input Format
The 1st line will contain an integer T, the number of test cases. This is followed by T lines, each containing an integer N. i.e. the number of digits in the number.

Output Format
Largest Decent Number having N digits. If no such number exists, tell Sherlock that he is wrong and print ?1.

Constraints
1?T?20
1?N?100000


Sample Input

4
1
3
5
11
Sample Output

-1
555
33333
55555533333
Explanation
For N=1, there is no such number.
For N=3, 555 is the only possible number.
For N=5, 33333 is the only possible number.
For N=11, 55555533333 and all permutations of these digits are valid numbers; among them, the given number is the largest one.
"""

for _ in range(int(raw_input())):
    n = int(raw_input())
    r3 = (n / 3)
    q3 = (n % 3)
    if q3 != 0 and r3 > 1:
        while q3 % 5 != 0:
            if r3 == 1:
                break
            r3 -= 1
            q3 = q3 + 3
    elif q3 != 0 and r3 == 1:
        r3 = 0
    if q3 % 5 != 0:
        r3 = 0
    r5 = (n / 5)
    q5 = (n % 5)
    if q5 != 0 and r5 > 1:
        while q5 % 3 != 0:
            if r5 == 1:
                break
            r5 -= 1
            q5 = q5 + 5
    elif q5 != 0 and r5 == 1:
        r5 = 0
    if q5 % 3 != 0:
        r5 = 0
    #print r3, q3
    #print r5, q5
    s = ""
    if r3 == r5 == 0 or ((r3 * 3 + q3) != n and (r5 * 5 + q5) != n):
        s = "-1"
    elif r3 > r5:
        r = r3 * 3
        for i in range(r):
            s += "5"
        for i in range(n-r):
            s += "3"
    else:
        r = r5 * 5
        for i in range(r):
            s += "3"
        for i in range(n-r):
            s += "5"
    print s
    #print
