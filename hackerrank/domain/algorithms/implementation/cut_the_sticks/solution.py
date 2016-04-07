n = int(input())
l = input().split()
sorted_list = []
for i in l:
    sorted_list.append(int(i))
sorted_list.sort()
sorted_list.reverse()
while sorted_list.__len__() != 0:
    count = sorted_list.__len__()
    val = sorted_list.pop()
    num = sorted_list.count(val)
    for i in range(0, num):
        sorted_list.remove(val)
    l = []
    for i in range(0, sorted_list.__len__()):
        l.append(sorted_list.pop() - val)
    sorted_list = sorted(l)
    sorted_list.reverse()
    print (count)