"""
You will be given a list of 32 bits unsigned integers. You are required to
output the list of the unsigned integers you get by flipping bits in its
binary representation (i.e. unset bits must be set, and set bits must be
unset).

Input Format

The first line of the input contains the list size TT, which is followed by
TT lines, each line having an integer from the list.

Constraints

1<=T<=100
0<=integer<232
Output Format

Output one line per element from the list with the requested result.

Sample Input

3
2147483647
1
0
Sample Output

2147483648
4294967294
4294967295
Explanation

Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001
and doing the flipping we get 11111111111111111111111111111110 which in turn
is 4294967294.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def convert_to_binary(N):
    n = 0
    if N:
        n = int(math.floor(math.log10(N)/math.log10(2)) + 1)
    #bin = [0 for i in range(32)]
    bin = [0 for i in range(n)]
    i = n - 1
    while(N!=0):
        bin[i] = N % 2
        N /= 2
        i -= 1
    l = list(map(str, bin))
    if len(l) < 32:
        length = len(l)
        for i in range(32 - length):
            l.insert(0, '0')
    s = "".join(l)
    return s


def convert_to_decimal(s):
    n = len(s)
    N = 0
    while n > 0:
        if s[len(s) - n] == '0':
            N += math.pow(2,n-1)
        n -= 1
    return int(N)


t = int(raw_input())
for i in range(t):
    b = convert_to_binary(int(raw_input()))
    #print b
    print convert_to_decimal(b)