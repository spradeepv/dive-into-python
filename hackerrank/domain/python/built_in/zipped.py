"""
Task

The National University, conducts an examination of N students in X subjects.
Your task is to compute average scores of each student.

Average score=Sum of scores obtained in all subjects by a studentTotal number of subjects
The format for general mark sheet is :

Student ID ? ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5
Input Format

First line contains, space separated values of N and X.
Next X lines contains, space separated marks obtained by students in a particular subject.

Constraints

0<N?100
0<X?100
Output Format

Print averages of all students in separate lines.

Averages must be correct upto 1 decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
Sample Output

90.0
91.0
82.0
90.0
85.5
Explanation

Marks obtain by student 1 : 89, 90, 91
Average marks of student 1 : 270 / 3 = 90

Marks obtain by student 2 : 90, 91, 92
Average marks of student 1 : 273 / 3 = 91

Marks obtain by student 3 : 78, 85, 83
Average marks of student 1 : 246 / 3 = 82

Marks obtain by student 4 : 93, 88, 89
Average marks of student 1 : 270 / 3 = 90

Marks obtain by student 5 : 80, 86, 90.5
Average marks of student 1 : 256.5 / 3 = 85.5
"""

n, x = map(int, raw_input().split())
l = []
for i in range(x):
    l.append(map(float, raw_input().split()))
#print l, zip(*l)
for tup in zip(*l):
    total = 0
    for i in range(x):
        total += tup[i]
    avg = total/x
    print avg