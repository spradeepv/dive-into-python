from collections import defaultdict
s = raw_input()
vowels = ['A', 'E', 'I', 'O', 'U']

points = [0, 0]
for i, c in enumerate(s):
    points[c in vowels] += len(s) - i

if points[0] > points[1]:
    print "Stuart", points[0]
elif points[1] > points[0]:
    print "Kevin", points[1]
else:
    print "Draw"


def get_all_substrings(s):
    length = len(s)
    return [s[i: j] for i in xrange(length) for j in xrange(i + 1, length + 1)]

def get_points(substring, s):
    points = 0
    index = s.find(substring)
    while index != -1:
        points += 1
        index = s.find(substring, index+1)
    #print substring, points
    return points

