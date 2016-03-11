"""
A balanced string is a string having the following properties:

Both the left and right halves contain the same characters.
Both the left and right halves contain unique characters.
For example, abbaabba is balanced because the left half (abab) and the right
half (baba) both contain the same unique characters.

Xavier has NN unique characters in unlimited supply and wants to use them to
make balanced strings. Help him determine PP, the number of possible
balanced strings of length NN.

Input Format

The first line contains an integer, TT, the number of test cases.
The TT subsequent lines each contain a single integer, NN, the number of
characters Xavier can use to form his balanced strings for that test case.

Constraints

N will always be evenN will always be even
Xavier's balanced strings must be of length NXavier's balanced strings must
be of length N
Output Format

For each test case, print the result of P % (109+7)P % (109+7) on a new line.

Constraints

1<=T<=100000
2<=N<=10^6
Sample Input

1
2
Sample Output

2
Explanation

N=2
Xavier has two characters we'll refer to as 1 and 2. He must use these
characters to form balanced strings of length 22. The possible strings are
"11", "12", "21", and "22". Of those 44 strings, only 22 are
balanced (i.e.: "11" and "22"), so we print the result of 2 % (10^9+7)2 on a
new line.

Editorial
---------

N  is even number so to make string balance right half and left half both
having N/2 characters should contains equal and same set of characters.
For right half Xrange have N unique characters so there will be N*(N-1)*(
N-2)*......(N/2+1) possible strings that can be
formed with N unique characters.
For each right half string there will be (N/2)! possible left half
strings. So the answer will be N*(N-1)*(N-2)*....(N/2+1)*((N/2)!) that will
be equal to N!
"""
mod = int(1e9) + 7
fact = [1, 1]
def facto():
    for i in range(2, 1000001):
        fact.append((fact[-1]*i) % mod)

facto()
for _ in range(int(raw_input())):
    n = int(raw_input())
    print fact[n]
