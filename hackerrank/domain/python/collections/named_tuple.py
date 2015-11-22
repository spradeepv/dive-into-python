"""
Problem Statement

collections.namedtuple()

namedtuples are basically easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples you don't have to use integer indexes for accessing members
of a tuple.

Example

Code 01

from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print dot_product
11

Code 02

from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print xyz.Class
Y
Task

Dr. John Wesley, has a spreadsheet containing list of student's IDs, marks, class and name.

Your task is to help Dr. Wesley in computing the average marks of students.

Average=Sum of all marksTotal Students

Note:
1. Columns can be in any order, i.e., IDs, marks, class and name can be written in any order in spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (Spelling and case of these names won't change)

Input Format

First line contains an integer N, the total number of students.
Second line contains the name of columns.
Next N lines contain the marks, id, name and class, under their respective column names.

Constraints

0<N?100
Output Format

Print the average marks.(correct upto 2 decimal places)

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
TESTCASE 02

5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00
Explanation

TESTCASE 01

Average = (97+50+91+72+80)/5

Can you solve this challenge in 4 lines of code or less?
There is no penalty for solutions which are correct but have more than 4 lines.
"""
from collections import namedtuple
n = int(raw_input())
Student = namedtuple('Student', '{0}'.format(",".join(raw_input().split())))
sum = 0
for _ in range(n):
    r = raw_input().split()
    s = Student(r[0], r[1], r[2], r[3])
    sum += int(s.MARKS)
print "{:.2f}".format(float(sum)/n)