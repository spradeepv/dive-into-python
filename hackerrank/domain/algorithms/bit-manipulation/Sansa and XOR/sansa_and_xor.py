for _ in range(int(raw_input())):
    n = int(raw_input())
    l = map(int, raw_input().split())
    if n % 2 == 0:
        print 0
    else:
        ans = 0
        for i in range(0, n + 1, 2):
            ans ^= l[i]
        print ans