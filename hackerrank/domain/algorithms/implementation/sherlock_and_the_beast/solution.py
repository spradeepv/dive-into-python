for _ in range(int(raw_input())):
    n = int(raw_input())
    r3 = (n / 3)
    q3 = (n % 3)
    if q3 != 0 and r3 > 1:
        while q3 % 5 != 0:
            if r3 == 1:
                break
            r3 -= 1
            q3 = q3 + 3
    elif q3 != 0 and r3 == 1:
        r3 = 0
    if q3 % 5 != 0:
        r3 = 0
    r5 = (n / 5)
    q5 = (n % 5)
    if q5 != 0 and r5 > 1:
        while q5 % 3 != 0:
            if r5 == 1:
                break
            r5 -= 1
            q5 = q5 + 5
    elif q5 != 0 and r5 == 1:
        r5 = 0
    if q5 % 3 != 0:
        r5 = 0
    #print r3, q3
    #print r5, q5
    s = ""
    if r3 == r5 == 0 or ((r3 * 3 + q3) != n and (r5 * 5 + q5) != n):
        s = "-1"
    elif r3 > r5:
        r = r3 * 3
        for i in range(r):
            s += "5"
        for i in range(n-r):
            s += "3"
    else:
        r = r5 * 5
        for i in range(r):
            s += "3"
        for i in range(n-r):
            s += "5"
    print s
    #print
