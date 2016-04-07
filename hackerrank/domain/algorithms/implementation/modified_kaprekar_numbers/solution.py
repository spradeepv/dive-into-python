def kaprekar(n):
    l = str(n * n)
    length = len(l)
    right = l[0:length/2]
    if right == '':
        right = 0
    left = l[length/2:]
    if left == '':
        left = 0
    return n == int(right) + int(left)

p = int(raw_input())
q = int(raw_input())
answer = ""
for i in range(p, q+1):
    if kaprekar(i):
        answer += str(i)+" "
if len(answer) == 0:
    print ("INVALID RANGE")
else:
    print (answer)
