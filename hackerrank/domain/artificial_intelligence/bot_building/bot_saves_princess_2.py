"""
In this version of "Bot saves princess", Princess Peach and bot's position
are randomly set. Can you save the princess?

Task

Complete the function nextMove which takes in 4 parameters - an integer N,
integers r and c indicating the row & column position of the bot and the
character array grid - and outputs the next move the bot makes to rescue the
princess.

Input Format

The first line of the input is N (<100), the size of the board (NxN). The
second line of the input contains two space separated integers, which is the
position of the bot.

Grid is indexed using Matrix Convention

The position of the princess is indicated by the character 'p' and the
position of the bot is indicated by the character 'm' and each cell is
denoted by '-' (ascii value: 45).

Output Format

Output only the next move you take to rescue the princess. Valid moves are
LEFT, RIGHT, UP or DOWN

Sample Input

5
2 3
-----
-----
p--m-
-----
-----
Sample Output

LEFT
Resultant State

-----
-----
p-m--
-----
-----
Explanation

As you can see, bot is one step closer to the princess
"""


def nextMove(n, r, c, grid):
    #print grid
    my_pos_x = r
    my_pos_y = c
    princess_pos_x = 0
    princess_pos_y = 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'p':
                princess_pos_x = x
                princess_pos_y = y
    #print "My Position: ", my_pos_x, my_pos_y
    #print "Princess Position: ", princess_pos_x, princess_pos_y
    next_move = ""
    if my_pos_x != princess_pos_x:
        if my_pos_x > princess_pos_x:
            # Princess is above me
            next_move = "UP"
        elif my_pos_x < princess_pos_x:
            # Princess is below me
            next_move = "DOWN"
    elif my_pos_y != princess_pos_y:
        if my_pos_y > princess_pos_y:
            # Princess is to my left side
            next_move = "LEFT"
        elif my_pos_y < princess_pos_y:
            # Princess is to my right side
            next_move = "RIGHT"
    return next_move

n = int(raw_input())
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(list(raw_input().strip()))

print nextMove(n, r, c, grid)


