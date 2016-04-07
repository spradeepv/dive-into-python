"""
Problem Statement

Your algorithms have become so good at predicting the market that you now
know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for
the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of
WOT that you own, or not make any transaction at all. What is the maximum
profit you can obtain with an optimum trading strategy?

Input

The first line contains the number of test cases T. T test cases follow:

The first line of each test case contains a number N. The next line contains
N integers, denoting the predicted price of WOT shares for the next N days.

Output

Output T lines, containing the maximum profit which can be obtained for the
corresponding test case.

Constraints

1 <= T <= 10
1 <= N <= 50000

All share prices are between 1 and 100000

Sample Input

3
3
5 3 2
3
1 2 100
4
1 3 1 2
Sample Output

0
197
3
Explanation

For the first case, you cannot obtain any profit because the share price
never rises.
For the second case, you can buy one share on the first two days, and sell
both of them on the third day.
For the third case, you can buy one share on day 1, sell one on day 2,
buy one share on day 3, and sell one share on day 4.
"""
def days_to_sell(price_list, n):
    sell_on = [False for x in range(n)]
    local_max = -1
    for i in range(n-1, -1, -1):
        if price_list[i] > local_max:
            local_max = price_list[i]
            sell_on[i] = True
    return sell_on

for _ in range(int(raw_input())):
    n = int(raw_input())
    price_list = map(int, raw_input().split())
    sell_on = days_to_sell(price_list, n)
    shares = 0
    profit = 0
    investment = 0
    for i in range(n):
        if sell_on[i]:
            profit += price_list[i] * shares - investment
            shares = 0
            investment = 0
        else:
            shares += 1
            investment += price_list[i]
    print profit