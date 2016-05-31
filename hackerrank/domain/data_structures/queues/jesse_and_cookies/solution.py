import heapq

n, k = map(int, raw_input().split())
l = map(int, raw_input().split())
heapq.heapify(l)
index = 0
while l[0] <= k:
    if len(l) == 1:
        break
    x = heapq.heappop(l)
    y = heapq.heappop(l)
    z = x + (2 * y)
    heapq.heappush(l, z)
    index += 1
if not l or l[0] < k:
    print -1
else:
    print index