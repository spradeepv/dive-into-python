"""
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.
"""

def count7(N):
    m = N % 10
    N = N / 10
    if N == 0:
        return int(m == 7)
    return count7(N) + int(m == 7)

print count7(717)