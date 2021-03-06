"""
Task
Students of District College have subscription of English and French newspapers. Some students have subscribed to only English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of roll numbers of students, who have subscribed to English and French newspapers. Your task is to find total number of students who have subscribed to English or French newspapers but not both.

Input Format

First line contains, number of students who have subscribed to English newspaper.
Second line contains, space separated list of roll numbers of students, who have subscribed to English newspaper.
Third line contains, number of students who have subscribed to French newspaper.
Fourth line contains, space separated list of roll numbers of students, who have subscribed to French newspaper.

Constraints

0<Total number of students in college<1000
Output Format

Output total number of students who have subscriptions of English or French newspaper but not both.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

8
Explanation

Roll numbers of students who have subscriptions of English or French newspaper but not both:
4, 5, 7, 9, 10, 11, 21 and 55.
Hence, total is 8 students.
"""

n1 = int(raw_input())
english = set(map(int, raw_input().split()))
n2 = int(raw_input())
french = set(map(int, raw_input().split()))
print len(english.symmetric_difference(french))