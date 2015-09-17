"""
Task
You have a non-empty set s and you have to execute N commands given in N lines.

Commands will be pop, remove and discard.

Input Format

First line contains integer n, number of elements in set.
Second line contains space separated elements of set s. All elements are non-negative integers, less than or equal to 9.
Third line contains integer N, number of commands.
Next N lines contains pop, remove and discard commands.

Constraints

0<n<20
0<N<20
Output Format

Print sum of elements of set 's' in output.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Sample Output

4
Explanation

On application of these 10 operations on set, we get set([4]). Hence, sum is 4.

Note : Convert elements of set s to integers while assigning. To ensure proper input of set we have added, first two lines of code to the editor.


"""
n = int(raw_input())
s = set(map(int, raw_input().split()))
ops = int(raw_input())
for i in range(ops):
    l = raw_input().split()
    if len(l) > 1:
        getattr(s, l[0])(int(l[1]))
    else:
        getattr(s, l[0])()
print sum(s)
