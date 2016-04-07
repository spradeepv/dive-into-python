t = int(input())
answer = 0
for i in range(t):
    B, W = str(input()).split()
    b = int(B)
    w = int(W)
    X, Y, Z = str(input()).split()
    x = int(X)
    y = int(Y)
    z = int(Z)
    if z >= x and z >= y:
        answer = (x * b) + (y * w)
    else:
        answer = (x * b) + (y * w)
        temp = 0
        if x < y:
            temp = (x * b) + (x * w) + (z * w)
        else:
            temp = (y * b) + (y * w) + (z * b)
        if temp < answer:
            answer = temp
    print (answer)
