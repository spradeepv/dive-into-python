import sys
import copy


def is_ok(map, optimal):
    if map['G'] == optimal and map['C'] == optimal and map['T'] == optimal \
            and map['A'] == optimal:
        return True
    return False


n = int(raw_input())
s = raw_input()
map = {'G': 0, 'C': 0, 'T': 0, 'A': 0}
optimal = n / 4
for c in s:
    map[c] += 1

if is_ok(map, optimal):
    print 0
    sys.exit(1)

low = 0
high = n
print optimal
while high - low > 1:
    cont = False
    mid = (low + high) >> 1
    # print low, mid, high
    tmp = copy.deepcopy(map)
    for i in range(mid):
        tmp[s[i]] -= 1
    # print tmp
    if is_ok(map, optimal):
        # print"IF=1"
        # print tmp
        high = mid
        continue

    for i in range(mid, n):
        tmp[s[i - mid]] += 1
        tmp[s[i]] -= 1
        if is_ok(map, optimal):
            # print"IF=2"
            # print tmp
            high = mid
            cont = True
            break
    if not cont:
        low = mid
    # print "---------------"
    print tmp
    print low, mid, high
print high
