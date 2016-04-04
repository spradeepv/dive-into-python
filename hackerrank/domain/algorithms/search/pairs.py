n, k = map(int, raw_input().split())
list_a = map(int, raw_input().split())
set_a = set(list_a)
list_b = []
for i in set_a:
    list_b.append(i + k)
set_b = set(list_b)
print len(set_a.intersection(set_b))
