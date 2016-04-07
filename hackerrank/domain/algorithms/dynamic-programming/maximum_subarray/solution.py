def max_subarray(A):
    max_ending_here = max_so_far = 0
    length = len(A)
    if length > 1:
        for i in range(0, length):
            x = A[i]
            max_ending_here = max(0, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
            #print "max_ending_here : ",max_ending_here
            #print "max_so_far : ",max_so_far
    if max_so_far == 0:
        if len(A) == 1:
            return A[0]
        else:
            return -1
    else:
        return max_so_far


def max_subarray_non(A):
    max_ending_here = max_so_far = 0
    for x in A:
        if x > 0:
            max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        #print "max_ending_here : ",max_ending_here
        #print "max_so_far : ",max_so_far
    if max_so_far == 0:
        if len(A) == 1:
            return A[0]
        else:
            return -1
    else:
        return max_so_far

n = int(input())
strings = []
while n > 0:
    s = int(input())
    l = str(input()).split()
    li = []
    for i in l:
        li.append(int(i))
    s = repr((max_subarray(li))) + " " + repr(max_subarray_non(li))
    print (s)
    n -= 1
