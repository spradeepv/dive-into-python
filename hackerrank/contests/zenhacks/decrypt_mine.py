def shifttext(text, shift):
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) for char in text.lower())

for _ in range(int(raw_input())):
    p, e1 = raw_input().split()
    diff = 0
    l = []
    for i in range(len(p)):
        c = ord(p[i])
        c1 = ord(e1[i])
        d = abs(c - c1)
        print d
        if d != diff:
            diff = d
            t = shifttext(p, diff)
            if t not in l:
                l.append(t)
    print l
    diff_count = 101
    #print "diff", diff
    for i in l:
        diff = 0
        #print i, diff
        if i != e1:
            for j in range(len(i)):
                if e1[j] != i[j]:
                    diff += 1
        print i, diff, diff_count
        diff_count = min(diff, diff_count)
    print diff_count
