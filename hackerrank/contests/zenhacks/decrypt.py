for i in range(input()):
    p, e1 = map(str, raw_input().split())
    res = 10000000
    for i in range(26):
        cnt = 0
        t = ""
        for j in p:
            t += chr((ord(j) - ord('a') + i) % 26 + ord('a'))
        print t
        for j in range(len(p)):
            if t[j] != e1[j]:
                cnt += 1
        print cnt
        res = min(res, cnt)
    print res
