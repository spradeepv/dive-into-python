"""
Instead of storing the actual values in the array, you store the difference
between the current element and the previous element. So you add sum to a[p]
showing that a[p] is greater than its previous element by sum. You subtract
sum from a[q+1] to show that a[q+1] is less than a[q] by sum (since a[q] was
the last element that was added to sum). By the end of all this, you have an
array that shows the difference between every successive element. By adding
all the positive differences, you get the value of the maximum element
"""

n, m = map(int, raw_input().split())
a = [0] * (n + 1)
for i in range(m):
    p, q, k = map(int, raw_input().split())
    a[p] += k
    if q + 1 <= n:
        a[q + 1] -= k
        # print a
print a
x = 0
maximum = 0
for i in range(1, n + 1):
    x = x + a[i]
    if maximum < x:
        maximum = x
print maximum
