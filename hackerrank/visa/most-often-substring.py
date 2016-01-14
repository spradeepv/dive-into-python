def getsuffix(a, k, l):
    suff_list = []
    for i in range(0, len(a)):
        suff = a[i:]
        if len(suff) >= k and len(suff) <= l:
            suff_list.append(a[i:])
    #print "Suffix : ",l
    return suff_list

def getprefix(a, k, l):
    pre_list = []
    for i in range(1, len(a)+1):
        pref = a[:i]
        if len(pref) >= k and len(pref) <= l:
            pre_list.append(a[:i])
    #print "Prefix : ",l
    return pre_list

def get_substrings(a, k, l):
    s = tuple(a)
    subs = []
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            sub = a[index:index+size]
            if len(sub) >= k and len(sub) <= l and sub not in subs:
                subs.append(sub)
                yield sub



n = int(raw_input())
k, l, m = map(int, raw_input().split())
s = raw_input()
#print list(get_substrings(s, k, l))
max_count = 0
for sub in list(get_substrings(s, k, l)):
    #print sub, s.count(sub)
    if len(''.join(set(sub))) <= m:
        count = s.count(sub)
        if count > max_count:
            max_count = count
print max_count