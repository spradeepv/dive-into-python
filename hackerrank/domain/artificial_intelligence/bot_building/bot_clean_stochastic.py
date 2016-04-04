"""
A deterministic environment is one where the next state is completely
determined by the current state of the environment and the task executed by
the agent. If there is any randomness involved in determining the next
state, the environment is stochastic.

The game Bot Clean took place in a deterministic environment. In this
version, the bot is given 200 moves to clean as many dirty cells as
possible. The grid initially has 1 dirty cell. When the bot cleans this
cell, a new cell in the grid is made dirty. The new cell can be anywhere in
the grid.

The bot here is positioned at the top left corner of a 5*5 grid. Your task
is to move the bot to appropriate dirty cell and clean it.

Input Format
The first line contains two single spaced integers which indicates the
current position of the bot. The grid is indexed (x, y) 0<=x,y<=4 top to
bottom and left to right respectively. Refer to to board convention here.

5 lines follow showing the grid rows. Each cell in the grid is represented
by any of the following 3 characters:

'b' (ascii value 98) - the bot's current position (if on clean cell).

'd' (ascii value 100) - a dirty cell (even if the robot is present on top of
it).

'-' (ascii value 45) - a clean cell in the grid.

Sample Input

0 0
b---d
-----
-----
-----
-----
Output Format

Output is the action that is taken by the bot in the current step and it can
be any of the movements in 4 directions or cleaning the cell in which it is
currently located. The output formats are LEFT, RIGHT, UP and DOWN or CLEAN.
Output CLEAN to clean the dirty cell. Repeat this process until all the
cells on the grid are cleaned.

Sample Output

RIGHT
Resultant State

-b--d
-----
-----
-----
-----
The bot is positioned now at (0,1) and is 1 step closer to the dirty cell.
The next input will be

0 1
-b--d
-----
-----
-----
-----
Task

Complete the function nextMove that takes in 3 parameters posr, posc being
the co-ordinates of the bot's current position and board which indicates the
board state, and print the bot's next move.

Scoring

At the end of 200 moves, your score will be equal to the number of dirty
cell the bot has cleaned divided by 4.

Educational Links

https://en.wikipedia.org/wiki/Stochastic_game
"""
from functools import partial


def nextMove(bot_x, bot_y, board):
    dirty_cells = []
    for x in range(5):
        for y in range(5):
            if board[x][y] == 'd':
                dirty_cells.append((x, y))
                break
    # Get closest cell
    x = dirty_cells[0][0]
    y = dirty_cells[0][1]
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
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)