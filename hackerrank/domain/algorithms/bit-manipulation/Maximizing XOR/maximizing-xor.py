def max_xor(l, r):
    max = -1
    for i in range(l, r+1):
        for j in range(i, r+1):
            x = i ^ j
            if x > max:
                max = x
    return max

l = int(raw_input())
r = int(raw_input())
print max_xor(l, r)