"""
Princess Peach is trapped in one of the four corners of a square grid. You
are in the center of the grid and can move one step at a time in any of the
four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of
the grid. This is followed by an NxN grid. Each cell is denoted by '-' (
ascii value: 45). The bot position is denoted by 'm' and the princess
position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The
moves must be separated by '\n', a newline. The valid moves are LEFT or
RIGHT or UP or DOWN.

Sample input

3
---
-m-
p--
Sample output

DOWN
LEFT
Task

Complete the function displayPathtoPrincess which takes in two parameters -
the integer N and the character array grid. The grid will be formatted
exactly as you see it in the input, so for the sample input the princess is
at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on
consecutive lines to rescue/reach the princess. The goal is to reach the
princess in as few moves as possible.

The above sample input is just to help you understand the format. The
princess ('p') can be in any one of the four corners.

Scoring
Your score is calculated as follows : (NxN - number of moves made to rescue
the princess)/10, where N is the size of the grid (3x3 in the sample testcase).
"""


def displayPathtoPrincess(n,grid):
    #print grid
    my_pos_x = 0
    my_pos_y = 0
    princess_pos_x = 0
    princess_pos_y = 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'm':
                my_pos_x = x
                my_pos_y = y
            elif grid[x][y] == 'p':
                princess_pos_x = x
                princess_pos_y = y
    #print "My Position: ", my_pos_x, my_pos_y
    #print "Princess Position: ", princess_pos_x, princess_pos_y
    if my_pos_x > princess_pos_x:
        # Princess is above me
        diff_x = my_pos_x - princess_pos_x
        for _ in range(diff_x):
            print "UP"
    elif my_pos_x < princess_pos_x:
        # Princess is below me
        diff_x = princess_pos_x - my_pos_x
        for _ in range(diff_x):
            print "DOWN"
    if my_pos_y > princess_pos_y:
            # Princess is to my left side
            diff_y = my_pos_y - princess_pos_y
            for _ in range(diff_y):
                print "LEFT"
    elif my_pos_y < princess_pos_y:
        # Princess is to my right side
        diff_y = princess_pos_y - my_pos_y
        for _ in range(diff_y):
            print "RIGHT"


n = int(raw_input())
grid = []
for i in xrange(0, n):
    grid.append(list(raw_input().strip()))

displayPathtoPrincess(n, grid)

