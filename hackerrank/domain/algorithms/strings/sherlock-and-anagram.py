"""
Problem Statement
Given a string S, find the number of unordered anagramic pairs of substrings.
"""
import collections

def get_anagramic_pairs(s):
    d = collections.defaultdict(int)
    l = list(s)
    length = len(l)
    for i in range(length):
        for j in range(1, length - i + 1):
            sub = l[i: i + j]
            print i, j, sub
            sub.sort()
            d["".join(sub)] += 1
    print d
    num = 0
    for v in d.values():
        num += v * (v - 1) / 2
    return num

for _ in range(int(raw_input())):
    s = raw_input()
    print get_anagramic_pairs(s)