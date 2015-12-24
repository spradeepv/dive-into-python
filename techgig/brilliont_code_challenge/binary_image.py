def find_right(index, l):
    right_indices = []
    if index < len(l):
        while l[index + 1] == 1:
            right_indices.append(index)
            index += 1

def pixelValue(input1, input2):
    n, m = input1[0], input1[1]
    matrix = []
    while input2:
        for i in range(n):
            index = 1
            l = []
            for j in range(m):
                if index < input2[0]:
                    l.append(input2[1])
                    index += 1
                    if j == m - 1:
                        input2[0] = input2[0] - index + 1
                else:
                    l.append(input2[1])
                    input2.pop(0)
                    input2.pop(0)
                    index = 1
                if len(l) == m:
                    matrix.append(l)
    count = 0
    print matrix
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                left_index = None
                right_index = None
                top_index = None
                bottom_index = None
                if j != 0:
                    left_index = j - 1
                if j != m - 1:
                    right_index = j + 1
                if i != 0:
                    top_index = i - 1
                if i != n - 1:
                    bottom_index = i + 1
                # print left_index, right_index, top_index, bottom_index
                if left_index != None:
                    if matrix[i][left_index] != 1:
                        continue
                if right_index != None:
                    if matrix[i][right_index] != 1:
                        continue
                if top_index != None:
                    # print "****",matrix[top_index][j], top_index, j
                    if matrix[top_index][j] != 1:
                        continue
                if bottom_index != None:
                    if matrix[bottom_index][j] != 1:
                        continue
                count += 1
                # print "--->",count
    return count


input1 = [8, 9]
input2 = [11, 0, 2, 1, 2, 0, 3, 1, 7, 0, 2, 1, 10, 0, 17, 1, 3, 0, 4, 1, 2, 0,
          3, 1, 6, 0]

input_1 = [51, 101]
input_2 = [191, 0, 2, 1, 97, 0, 4, 1, 4, 0, 2, 1, 92, 0, 3, 1, 98, 0, 3, 1, 3,
           0, 3, 1, 92, 0, 3, 1, 3, 0, 3, 1, 78, 0, 8, 1, 11, 0, 4, 1, 77, 0,
           9, 1, 13, 0, 1, 1, 78, 0, 9, 1, 7, 0, 4, 1, 82, 0, 8, 1, 7, 0, 5, 1,
           81, 0, 8, 1, 7, 0, 2, 1, 1, 0, 2, 1, 80, 0, 8, 1, 8, 0, 5, 1, 81, 0,
           7, 1, 7, 0, 5, 1, 85, 0, 1, 1, 1, 0, 2, 1, 99, 0, 3, 1, 91, 0, 9, 1,
           91, 0, 10, 1, 93, 0, 5, 1, 1, 0, 2, 1, 93, 0, 8, 1, 93, 0, 8, 1, 92,
           0, 9, 1, 95, 0, 7, 1, 94, 0, 6, 1, 94, 0, 7, 1, 91, 0, 10, 1, 92, 0,
           8, 1, 94, 0, 1, 1, 2, 0, 3, 1, 94, 0, 1, 1, 2350, 0]
# print pixelValue(input1, input2)
print pixelValue(input_1, input_2)
