#!/usr/bin/env python
from itertools import izip
from bisect import bisect_left

def sort_suff(ss):
    sub_ss = set()
    for s in ss:
        for i in xrange(len(s)):
            sub_ss.add(buffer(s, i, len(s) - i))
    return sorted(sub_ss)

def get_lcp(s1, s2):
    print s1, "-", s2
    retval = 0
    for c1, c2 in izip(s1, s2):
        print "c1, c2: ", c1, c2
        if c1 == c2: retval += 1
        else: break
    return retval

def get_rank(suff_arr):
    rank = []
    for i, suff in enumerate(suff_arr):
        print i, suff
        if i == 0:
            rank.append(len(suff) - 1)
        if i > 0:
            prev_suff = suff_arr[i-1]
            lcp = get_lcp(prev_suff, suff)
            print "lcp :",lcp, rank[-1], len(suff[lcp:])
            rank.append(rank[-1] + len(suff[lcp:]))
    print rank
    return rank

n = int(raw_input())
ss = []
for _ in xrange(n):
    ss.append(raw_input())

suff_arr = sort_suff(ss) 
rank = get_rank(suff_arr)

def query(k):
    closet_rank_idx = bisect_left(rank, k)
    if closet_rank_idx == len(rank):
        return 'INVALID'
    closet_rank = rank[closet_rank_idx]
    print suff_arr[1]
    suff = suff_arr[closet_rank_idx]
    if closet_rank == k:
        return suff
    else:
        return suff[:k - closet_rank]

q = int(raw_input())
for _ in xrange(q):
    k = int(raw_input())
    print query(k-1)


