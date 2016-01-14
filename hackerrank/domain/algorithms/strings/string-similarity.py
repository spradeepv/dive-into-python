def stringSimilarity(inputs):
    ret = []
    for a in inputs:
        n = len(a)
        z = [0]*n
        l=r=0
        for i in range(1,n):
            if (i<=r):
                z[i]=min (r - i + 1, z[i - l])
            while(i + z[i] < n and a[z[i]] == a[i + z[i]]):
                z[i]+=1
            if (i + z[i] - 1 > r):
                l = i
                r = i + z[i] - 1
        ret.append(sum(z)+n)
    return ret

inputs = []
for _ in range(int(raw_input())):
    inputs.append(raw_input())

for i in stringSimilarity(inputs):
    print i

