n = int(input())
l = []
for i in range(0, n):
    l.append(int(input()))
for orig_num in l:
    count = 0
    num = orig_num
    while num != 0:
        digit = num % 10
        if digit == 0:
            pass
        elif orig_num % digit == 0:
            count += 1
        num = int(num / 10)
    print (count)