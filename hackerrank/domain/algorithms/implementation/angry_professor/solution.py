n = int(input())
for i in range(0, n):
    a, b = input().split()
    a, b = int(a), int(b)
    count = 0
    list = input().split()
    for j in list:
        c = int(j)
        if c <= 0:
            count += 1
    if count >= b:
        print ("NO")
    else:
        print ("YES")