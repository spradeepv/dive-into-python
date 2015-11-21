result = 0
m = {}
for _ in range(int(raw_input())):
    s = raw_input().split()
    key = s[0].strip()+"-"+s[1].strip()+"-"+s[2].strip()
    if m.has_key(key):
        l = m.get(key)
        l.append(s[3].strip())
    else:
        m.update({key: [s[3].strip()]})
#print m
for key, val in m.items():
    left = val.count('L')
    right = val.count('R')
    #print left, right
    if left != 0 and right != 0:
        result += left if left < right else right
print result
