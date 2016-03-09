# Enter your code here. Read input from STDIN. Print output to STDOUT
def common_child(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    len_1 = len(s1)
    len_2 = len(s2)
    table = [[0 for i in range(len_1)] for j in range(len_2)]
    for i in range(len_1):
        for j in range(len_2):
            if i == 0 and j == 0:
                table[i][j] = 1 if s1[0] == s2[0] else 0
            elif i == 0:
                table[i][j] = table[0][j - 1]
            elif j == 0:
                table[i][j] = table[i - 1][0]
            elif s1[i] == s2[j]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    print table
    return table[len(s1) - 1][len(s2) - 1]


s1 = raw_input()
s2 = raw_input()
print common_child(s1, s2)