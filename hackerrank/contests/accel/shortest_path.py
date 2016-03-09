"""
You're lost in a city where the streets are laid out in a North-South and
East-West grid, and each parallel street is 11 unit apart. You ask a
stranger for directions, but the route they give you is not optimal! Their
directions will get you from your origin to your destination, but they also
take you far out of the way.

Given a string of directions composed of the characters NN (North),
EE (East), SS (South), and WW (West), minimize the directions that will take
you to your destination. Then sort the directions lexicographically and
print them.

Note: You can assume that the destination will not be the origin.

Input Format

A string composed of the four directional characters: NN, EE, SS, and WW.

Constraints

1<=|directions|<=1000001<=|directions|<=100000
origin#destinationorigin#destination
Output Format

Print the lexicographically sorted string of minimal directions.

Sample Input

NESNWES
Sample Output

E
"""
s = raw_input()
x = 0
y = 0
for c in s:
    if c == 'N':
        x += 1
    elif c == 'S':
        x -= 1
    elif c == 'E':
        y += 1
    elif c == 'W':
        y -= 1
#print x, y
path = ""
# Only East and West possible
if x == 0 and y != 0:
    if y > 0:
        l = ['E' for i in range(y)]
    else:
        l = ['W' for i in range(abs(y))]
    path = "".join(l)
# Only North and South possible
elif x != 0 and y == 0:
    if x > 0:
        l = ['N' for i in range(x)]
    else:
        l = ['S' for i in range(abs(x))]
    path = "".join(l)
elif x != 0 and y != 0:
    if y > 0:
        l = ['E' for i in range(y)]
        path += "".join(l)
    if x > 0:
        l = ['N' for i in range(x)]
        path += "".join(l)
    if x < 0:
        l = ['S' for i in range(abs(x))]
        path += "".join(l)
    if y < 0:
        l = ['W' for i in range(abs(y))]
        path += "".join(l)
print path