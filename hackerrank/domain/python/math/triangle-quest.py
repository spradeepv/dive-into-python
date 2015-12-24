"""

"""

for i in range(1, int(raw_input()) + 1):
    print reduce(lambda a, b: a * 10 + b,
                 map(lambda x: x if x < i else 2 * i - x, range(1, 2 * i)))
