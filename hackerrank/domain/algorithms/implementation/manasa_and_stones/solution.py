from __future__ import print_function


def get_last(num_of_stones, num1, num2):
    l = []
    for i in range(1, num_of_stones):
        l.append(((num1 * i) + (num2 * ((num_of_stones - 1) - i))))
    return l
n = int(input())
for i in range(0, n):
    l = []
    start = 0
    num_of_stones = int(input())
    a = int(input())
    b = int(input())
    l.extend(get_last(num_of_stones, a, b))
    l.extend(get_last(num_of_stones, b, a))
    li = sorted(list(set(l)))
    for item in li:
        print (item, end=" ")
    print()
