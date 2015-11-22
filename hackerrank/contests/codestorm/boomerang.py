"""
Problem Statement

Aborigines of a mysterious island love to play the Boomerang Game.

The game involves n aborigines (n>=2) numbered with consecutive integers from
1 to n. Before the game starts, all participants form a ring so their numbers
in a clockwise order match consecutive numbers 1,2,...n. The distances between
the adjacent participants are equal. When n=2, they stand in exact opposite
points of the ring.

During the game, aborigines throw boomerangs in turn. Each aborigines throw a
boomerang at the exact opposite point of the ring. The participant number 1
throws a boomerang first. Two things can happen:

If the number of aborigines is even, then the boomerang hits the participant
standing at the exact opposite point from the aborigine numbered 1.

If the number of participants is odd, the exact opposite point is empty. In
this case, the boomerang flies back and hits the aborigine who threw it.

The aborigine who has been hit by a boomerang leaves the game. The remaining
participants move around the ring so that the distances between the adjacent
aborigines becomes equal again. Note: The aborigines do not change their
order in the ring during this move.

The aborigine who was the closest in the clockwise direction to the aborigine
who threw a boomerang last will go next. Again, only one of the two scenarios
listed above can happen. After that, the aborigines move again to make the
distance between the adjacent participants equal. The next turn belongs to the
closest participant in a clockwise order and so on.

The aborigines will continue to play and throw boomerangs until there is only
one participant left. He or she will be the winner.

Determine the winning aborigine's number for the given number of participants n.

Input Format

The first line contains the number of test cases: T. Each of the next T lines
contains a single integer: n.

Constraints

For full score:
1<=T?100000
2?n?1018

For 40% score:
1<=T?100000
2?n?1000

Output Format

Output T lines, one corresponding to each test case.

Sample Input

6
2
3
4
5
10
1000
Sample Output

1
2
4
5
5
818
"""
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    N = int(raw_input().strip())
    players = [x for x in range(1, N+1)]
    player_index = 0
    start = players[player_index]
    out = []
    in_game = []
    n = N
    while len(players) > 1:
        #print players
        length = len(players)
        if length%2 == 0:
            remove_index = player_index + length/2
            print ">>>>>>>",player_index, remove_index, length
            if remove_index >= length:
                if length == 2:
                    remove_index = remove_index % length
                else:
                    remove_index = remove_index % length
            print "---------", player_index, remove_index
            players.pop(remove_index)
            #if remove_index != 0 and player_index + 1 <= len(players):
            if remove_index != 0:
                player_index += 1
        else:
            print "********",player_index, length
            players.pop(player_index)
        #print "------>",player_index
        if player_index >= len(players):
            player_index = player_index - len(players)
    print players[0]