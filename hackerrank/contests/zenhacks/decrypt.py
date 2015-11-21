def shifttext(text, shift):
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) for char in text.lower())

for _ in range(int(raw_input())):
    s = raw_input().split()
    p = s[0]
    e1 = s[1]
    diff = 0
    l = []
    for i in range(len(p)):
        c = ord(p[i])
        c1 = ord(e1[i])
        d = abs(c - c1)
        #print d
        if d != diff:
            diff = d
            l.append(shifttext(p, diff))
    #print l
    diff_count = 101
    #print "diff", diff
    for i in l:
        diff = 0
        #print i, diff
        if i != e1:
            for j in range(len(i)):
                if e1[j] != i[j]:
                    diff += 1
        if diff < diff_count:
            if diff > 0 or (diff == 0 and len(l) == 1):
                diff_count = diff
    print diff_count
