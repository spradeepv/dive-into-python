import math


def squares_between(a, b):
    """Finds the number of square integers between a and b."""
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count

t = int(input())
answer = 0
for i in range(t):
    A, B = str(input()).split()
    a = int(A)
    b = int(B)
    print(int(squares_between(a, b)))
