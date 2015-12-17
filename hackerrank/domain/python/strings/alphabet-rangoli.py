"""
Problem Statement

You are given an integer, N. Your task is to print an alphabet rangoli of
size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary
has the Nth alphabet letter (in alphabetical order).

Input Format

Only one line of input containing N, the size of the rangoli.

Constraints

0<N<27
Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
N = int(raw_input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print alphabet[::-1]
x = ['-'.join(sublist) for sublist in [
    [alph for alph in alphabet[i:N]][::-1] + [alph for alph in alphabet[i:N]][
                                             1:] for i in range(N)]]
print x

x = x[::-1] + x[1:N]

for i in range(len(x)):
    print (x[i]).center(len(x[N - 1]), '-')

for i in (range(N) + range(N - 2, -1, -1)):
    s = "-".join(chr(ord('a') + N - j - 1) for j in range(i + 1))
    print((s + s[::-1][1:]).center(N * 4 - 3, '-'))

for i in (range(N) + range(N - 2, -1, -1)):
    #print i
    asc = ord('a') + N - 1
    s = "-".join(chr(asc - j) for j in range(i + 1))
    #print s
    print ((s + s[::-1][1:]).center(N*4-3, '-'))
