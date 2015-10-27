"""
Write a function called longestRun, which takes as a parameter a list of
integers named L (assume L is not empty). This function returns the length of
the longest run of monotonically increasing numbers occurring in L. A run of
monotonically increasing numbers means that a number at position k+1 in the
sequence is either greater than or equal to the number at position k in the
sequence.

For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should
return the value 5 because the longest run of monotonically increasing integers
in L is [3, 4, 5, 7, 7].


You may find it useful to use the function getSublists as defined above but
you do not have to use this function. If you do use getSublists, the graders
will use our implementation for getSublists. In the box for this problem,
only paste the definition for the function longestRun.

Hint if you are Using getSublists

Your function does not have to be recursive. Do not leave any debugging print
statements when you paste your code in the box.
"""
from problem_4_1 import getSublists

def longestRun(L):
    longest = 1
    for n in range(2, len(L)+1):
        l = getSublists(L, n)
        is_break = False
        print l
        for i in l:
            temp = 1
            for j in range(len(i)):
                if j+1 < len(i) and i[j] <= i[j+1]:
                    temp += 1
                else:
                    is_break = True
                    break
        print temp
        if temp > longest:
            longest = temp
    return longest

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
L = [-10, -5, 0, 5, 10]
L = [1, 1, 1, 1, 1]
L = [1, 2, 3, -1, -2, -3, -4, -5, -6]
print longestRun(L)