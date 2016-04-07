for _ in range(int(raw_input())):
    n = int(raw_input())
    h = 1
    for i in range(n):
        if i % 2 == 0:
            h *= 2
        else:
            h += 1
    print h
