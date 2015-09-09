def is_sherlock_array(N, A):
    f = [0 for _ in xrange(N+1)]
    for i in xrange(1, N+1):
        f[i] = f[i-1]+A[i-1]
    for i in xrange(N):
        if f[i]==f[N]-f[i+1]:
            return "YES"
    return "NO"

def get_input():
    test_cases = int(raw_input())
    for i in range(test_cases):
        n = int(raw_input())
        arr = map(int, raw_input().split())
        #print arr
        print is_sherlock_array(n, arr)

get_input()
