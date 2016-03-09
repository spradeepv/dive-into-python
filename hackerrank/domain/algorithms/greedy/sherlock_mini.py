# Hi all this is an NlogN solution
# the idea is like this:
# first you sort the A array, you will have something like the following
# 2 7 25 28 38
# suppose your P is 4 and you Q is 32
# then you need to divide your input range to three parts:
# 4-7,7-28,28-32
# for the 4-7 part, you first calculate 7-4=3, and compare it to (7-2)/2=2, and take the minimum. So the maximum you can achieve in the first input range is 2, when input is 2+(7-2)/2=4
# likewise, for the 28-32 part, you can similarly calculate the maximum 4 can be achieved when input is 32
# for the 7-28 range, you take the maximum of all the half-distances between each consecutive A[i] value. For example, in this case it will be max((25-7)/2, (28-25)/2). You also need to keep track of the input as well.
# if you have the three pieces, for the answer you just need to take the maximum of them.
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
A = [int(i) for i in raw_input().split()]
P,Q = [int(i) for i in raw_input().split()]
A.sort()
#find left index
idx_l = 0
for val in A:
    if val < P:
        idx_l += 1
    else:
        break
#find right index
idx_r = len(A)-1
for val in reversed(A):
    if val > Q:
        idx_r -= 1
    else:
        break
#if idx_r is -1, it means Q is less than the minimum of A
#if idx_l is the same as idx_r
print idx_l, idx_r
#find the max inside left and right index
if idx_r>idx_l:
    max_inside = 0
    for i in range(idx_l,idx_r):
        if (A[i+1] - A[i])/2 > max_inside:
            max_inside = (A[i+1] - A[i])/2
            max_inside_idx = A[i] + max_inside
else:
    max_inside = 0
    max_inside_idx = 0
#deal with extra inputs
#distance between left extra with nearest
max_left = 0
max_left_idx = P
if A[idx_l] != P:
    if idx_l == 0:
        #dont worry about left value anymore
        max_left = A[0]-P
    else:
        #need to consider left value
        max_left = A[idx_l]-P
        if max_left > (A[idx_l] - A[idx_l-1])/2:
            max_left = (A[idx_l] - A[idx_l-1])/2
            max_left_idx = A[idx_l-1] + max_left

max_right = 0
max_right_idx = Q
if A[idx_r] != Q:
    if idx_r == len(A)-1:
        #dont worry about right value anymore
        max_right = Q - A[idx_r]
    else:
        #need to consider right value
        max_right = Q - A[idx_r]
        if max_right > (A[idx_r+1] - A[idx_r])/2:
            max_right = (A[idx_r+1] - A[idx_r])/2
            max_right_idx = A[idx_r] + max_right
print max_left, max_inside, max_right
print max_left_idx, max_inside_idx, max_right_idx
if max_left>=max_inside and max_left>=max_right:
    print max_left_idx
elif max_inside>=max_left and max_inside>=max_right:
    print max_inside_idx
else:
    print