"""
Task

Now, lets use our knowledge of Sets and help 'Mickey'.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 'Mickey' to compute an average of all the plants with distinct heights in her greenhouse.

Formula used:
Average=SumofDistinctHeightsTotalNumberofDistinctHeights
Input Format

First line contains, total number of plants in greenhouse.
Second line contains, space separated height of plants in the greenhouse.
Total number of plants is upto 100 plants.

Output Format

Output the average value of height.

Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375
Explanation

set([154, 161, 167, 170, 171, 174, 176, 182]), is the set containing distinct heights. Using sum() and len() functions we can compute the average.

Average=13558=169.375
"""

from __future__ import division
n = int(raw_input())
l = map(int, raw_input().split())
s = set(l)
avg_ht = sum(s)/len(s)
print "{:.3f}".format(avg_ht)
