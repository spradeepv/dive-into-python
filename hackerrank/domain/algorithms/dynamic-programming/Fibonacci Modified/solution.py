l = str(input()).split()
a = int(l[0])
b = int(l[1])
n = int(l[2])
for x in range(3, n+1):
    answer = a + (b * b)
    a = b
    b = int(answer)
print (b)