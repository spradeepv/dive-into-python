"""
Tic-tac-toe is a pencil-and-paper game for two players, X (ascii value 88)
and O (ascii value 79), who take turns marking the spaces in a 3*3 grid. The
player who succeeds in placing three respective marks in a horizontal,
vertical, or diagonal row wins the game. Empty space is represented by _ (
ascii value 95), and the X player goes first.

Here is an example game won by the first player, X:

picture alt

The function nextMove takes in a char player, and the 3x3 board as an array.
Complete the function to print 2 space separated integers r and c which
denote the row and column that will be marked in your next move. The top
left position is denoted by (0,0).

How does it work?
Your code is run alternately with the opponent bot for every move.

Example input:

X
___
___
_XO
Example output:

1 0
Explanation:
The board results in the following state after the above move

___
X__
_XO
"""
# !/bin/python
import random


# Complete the function below to print 2 integers separated by a single
# space which will be your next move
def nextMove(player, board):
    print board


# If player is X, I'm the first player.
# If player is O, I'm the second player.
player = raw_input()

# Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append([x for x in raw_input().strip()])

nextMove(player, board)
