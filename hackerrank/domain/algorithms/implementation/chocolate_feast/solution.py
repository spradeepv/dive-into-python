T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    n = int(N)
    c = int(C)
    m = int(M)
    answer = 0
    no_of_choc = n / c
    rem_choc = 0
    while c > 0:
        c = 0
        answer += no_of_choc
        no_of_choc += rem_choc
        if no_of_choc >= m:
            c += no_of_choc / m
            rem_choc = no_of_choc % m

            if (c + rem_choc) < m:
                rem_choc = 0
            no_of_choc = int(c)
    print(int(answer))
