"""
Editorial
---------
Solution: Find OR of all the elements and multiply it with 2^(n-1) where n
is the total number of elements. This gives us the answer.
Idea:
There will be total 2^n subsets.
If ith bit of any element is set, then that bit will be set in xor of half
of the total subsets which is 2^(n-1).
To find out all the set bits in all the numbers we find OR of all the numbers.
Since each set bit appears in half of the total subsets we multiply OR of
all numbers with 2^n-1 to get the final result.
"""
for _ in range(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    answer = a[0]
    for i in range(1, n):
        answer |= a[i]
    print (answer * pow(2, n-1)) % (pow(10, 9) + 7)