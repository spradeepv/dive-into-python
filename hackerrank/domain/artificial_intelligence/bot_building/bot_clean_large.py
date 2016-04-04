"""
In this challenge, you must program the behaviour of a robot.

The robot is positionned in a cell in a grid G of size H*W. Your task is
to move the robot through it in order to clean every "dirty" cells.

Input Format

The first line contians the position x and y of the robot.

The next line contains the height H and the width W of the grid.ille.

The H next lines represent the grid G. Each cell is represented by one of
those three characters:

'b' for the position of the robot
'd' for a dirty cell
'-' for a clean cell
If the robot is on a dirty cell, the character 'd' will be used.

Constraints
1<=W<=50
1<=H<=50
Output Format

You must print the next action the robot will perform. Here are the five
possibilities:

LEFT
RIGHT
UP
DOWN
CLEAN
It's important you understand that the input you get is a specific
situation, and you must only print the next action to perform. You program
will be called iteratively several times so that the robot cleans all the grid.

Sample Input

0 0
5 5
b---d
-d--d
--dd-
--d--
----d
Sample Output

RIGHT
Resultant state

-b--d
-d--d
--dd-
--d--
----d
"""
from functools import partial


def next_move(bot_x, bot_y, height, width, board):
    dirty_cells = []
    for x in range(height):
        for y in range(width):
            if board[x][y] == 'd':
                dirty_cells.append((x, y))
    # Get closest cell
    dist = lambda s, d: (s[0]-d[0]) ** 2 + (s[1]-d[1]) ** 2
    closest_dirty_cell =  min(dirty_cells, key=partial(dist, (bot_x, bot_y)))
    x = closest_dirty_cell[0]
    y = closest_dirty_cell[1]
    move = ""
    if bot_x != x:
        if bot_x > x:
            move = "UP"
        else:
            move = "DOWN"
    elif bot_y != y:
        if bot_y > y:
            move = "LEFT"
        else:
            move = "RIGHT"
    else:
        move = "CLEAN"
    print move


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)