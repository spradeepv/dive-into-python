c = 0
def get_count(num1, num2):
    n1 = bin(int(num1))
    s1 = repr(n1)
    count1 = s1.count('1')
    n2 = bin(int(num2))
    s2 = repr(n2)
    count2 = 0
    for i in range(2, s2.__len__()):
        if s2[i] == '1':
            count2 += 1
    if count1 == count2:
        global c
        c += 1
    if count1 > count2:
        global c
        c = 1
        return num1, count1
    else:
        return num2, count2
N, M = str(input()).split()
no_of_people = int(N)
no_of_subject = int(M)
l = []
for i in range(no_of_people):
    data = int(input(), 2)
    l.append(data)
highest = 0
count = 0
for i in range(0, l.__len__()):
    for j in range (i+1, l.__len__()):
        data = l[i] | l[j]
        highest, count = get_count(data, highest)
print (count)
print (c)