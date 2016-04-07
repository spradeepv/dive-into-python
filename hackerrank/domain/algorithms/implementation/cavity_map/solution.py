n = int(input())
matrix = [[0 for x in range(n)]for x in range(n)]
row = 0
for i in range(0, n):
    orig_num = int(input())
    count = 0
    num = orig_num
    col = n
    while num > 0:
        digit = int(num % 10)
        num = num / 10
        col -= 1
        matrix[row][col] = digit
    row += 1
for i in range(0, n):
    s = ""
    for j in range(0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            s += repr(matrix[i][j])
        else:
            left = matrix[i][j - 1]
            right = matrix[i][j + 1]
            up = matrix[i - 1][j]
            down = matrix[i + 1][j]
            current = matrix[i][j]
            if current > left and current > right and current > up and current > down:
                s += 'X'
            else:
                s += repr(matrix[i][j])
    print (s)
