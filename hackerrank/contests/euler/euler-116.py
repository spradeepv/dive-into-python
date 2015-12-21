def subset_sum(number, l):
    ways = [0] * (number + 1)
    ways[0] = 1
    for n in l:
        for j in xrange(n, number + 1):
            ways[j] += ways[j - n]
    print ways
    return ways[number]

print subset_sum(3, [2, 1])
