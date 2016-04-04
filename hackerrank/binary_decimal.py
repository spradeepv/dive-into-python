"""
0 - 0
1 - 1
2 - 10
3 - 11
4 - 100
5 - 101
6 - 110
7 - 111
8 - 1000
9 - 1001
10 - 1010
11 - 1011
12 - 1100
13 - 1101
14 - 1110
15 - 1111

2^0 = 1 + 0 = 1
2^1 = 2 + 1 = 3
2^2 = 4 + 3 = 7
2^3 = 8 + 7 = 15
2^4 = 16 + 15 = 31
2^5 = 32 + 31 = 63
2^6 = 64 + 63 = 127
2^7 = 128 + 127 = 255
2^8 = 256 + 255 = 511
2^9 = 512 + 511 = 1023
2^10 = 1024 + 1023 = 2047
2^11 = 2048 + 2047 = 4095
2^12 = 4096 + 4095 = 8191
2^13 = 8192 + 8191 = 16383
2^14 = 16384 + 16383 = 32767
2^15 = 32768 + 32767 = 65535
2^16 = 65536 + 65535 = 131071
2^17 = 131072 + 131071 = 262143
2^18 = 262144 + 262143 = 524287
2^19 = 524288 + 524287 = 1048575
"""
def swap_array(a):
    l = [pow(2, x) + (pow(2, x)-1) for x in range(20)]
    print l
    length = len(a)
    if length == 1:
        print a[0]
    else:
        a.sort()
        a.reverse()
        print a
        for index in range(length):
            if a[index] in l and index != 0:
                next_num = a[index] + pow(2, l.index(a[index]))
                print index, next_num
                i = index
                while True:
                    print i, a[i-1]
                    if i > 0 and a[i - 1] < next_num:
                        a[i], a[i-1] = a[i-1], a[i]
                        i -= 1
                    else:
                        break
                    print a
                #if next_num in a:
                #    j = a.index(next_num) + 1

        print a

def f(l):
    l.sort(lambda n:-bin(n).count('1'))


l = map(int, raw_input().split())
#swap_array(l)
l.sort()
l.reverse()
print(sorted(l,key=lambda x:-bin(int(x)).count("1")))