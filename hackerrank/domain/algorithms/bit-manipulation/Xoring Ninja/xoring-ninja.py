for _ in range(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    answer = a[0]
    for i in range(1, n):
        answer |= a[i]
    print (answer * pow(2, n-1)) % (pow(10, 9) + 7)
