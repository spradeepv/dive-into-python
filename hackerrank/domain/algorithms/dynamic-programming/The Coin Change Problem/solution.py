def subset_sum(number, l):
    ways = [0] * (number + 1)
    ways[0] = 1
    for n in l:
        for j in xrange(n, number + 1):
            ways[j] += ways[j - n]
        print ways
    return ways[number]

n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
print subset_sum(n, l)