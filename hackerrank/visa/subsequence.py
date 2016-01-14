    def kSub(k, nums):
        l = [0 for x in range(100)]
        sum = 0
        l[0] = 1
        for num in nums:
            sum += num
            if sum >= k:
                sum %= k
            l[sum] += 1
        ret = 0
        for i in range(k):
            ret += l[i] * (l[i] - 1)/2
        return ret


    k = int(raw_input())
    n = int(raw_input())
    for i in range(n):
        l = map(int, raw_input().split())
        print kSub(k, l)