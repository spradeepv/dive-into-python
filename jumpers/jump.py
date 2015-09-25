"""
There are 100 empty slots.
J1 to J5 are jumpers placed at position 2-6 respectively
J is one more jumper placed at position 1.
J1 to J5 can Jump 16 10 5 3 1 places respectively

Find the jump of J so that it will not collide with any other Jumper.
# If J1-J5 jumper collide with each other they are out of the game
# If Jump crosses the boundary 1-100 it will return in reverse order
Example:
a) If J1 is 98 , as it can jump 16 places, the new position wil be 86 and
   the flow is in reverse order.
b) If J1 is in 2 slot(reverse), the new position will be 14.
c) All the jumpers jump 100 times and J Jumper must not collide in any of the
   jumps.
"""

