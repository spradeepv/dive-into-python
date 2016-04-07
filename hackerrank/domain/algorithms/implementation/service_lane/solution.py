n, t = map(int, raw_input().split())
array = map(int, raw_input().split())
for _ in range(t):
    i, j = map(int, raw_input().split())
    vehicle = 3
    for x in range(i, j+1):
        vehicle = min(vehicle, array[x])
    print vehicle