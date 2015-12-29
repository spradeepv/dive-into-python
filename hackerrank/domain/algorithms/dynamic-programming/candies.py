"""
Problem Statement

Alice is a kindergarden teacher. She wants to give some candies to the
children in her class.  All the children sit in a line ( their positions are
fixed), and each  of them has a rating score according to his or her
performance in the class.  Alice wants to give at least 1 candy to each
child. If two children sit next to each other, then the one with the higher
rating must get more candies. Alice wants to save money, so she needs to
minimize the total number of candies given to the children.

Input Format

The first line of the input is an integer N, the number of children in
Alice's class. Each of the following N lines contains an integer that
indicates the rating of each child.

1 <= N <= 105
1 <= ratingi <= 105

Output Format

Output a single line containing the minimum number of candies Alice must buy.

Sample Input

3
1
2
2
Sample Output

4

Explanation

Here 1, 2, 2 is the rating. Note that when two children have equal rating,
they are allowed to have different number of candies. Hence optimal
distribution will be 1, 2, 1.

Input (stdin)
10
2
4
2
6
1
7
8
9
2
1

Expected Output

19
"""
ratings = []
n = int(raw_input())
candy_val = [1 for x in range(n)]
for i in range(n):
    rating = int(raw_input())
    ratings.append(rating)
    if i == 0:
        prev = rating
    else:
        next = rating
        if next > prev:
            candy_val[i] = candy_val[i - 1] + 1
        prev = next
for i in range(n-1, 0, -1):
    if ratings[i-1] > ratings[i]:
        candy_val[i-1] = max(candy_val[i-1], candy_val[i]+1)
print sum(candy_val)
