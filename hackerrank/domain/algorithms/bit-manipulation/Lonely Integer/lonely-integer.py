n = int(raw_input())
a = map(int, raw_input().split())
l = [0] * 101
for i in a:
    l[i] += 1
print l.index(1)