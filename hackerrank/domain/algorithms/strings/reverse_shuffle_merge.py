from collections import defaultdict


class ReverseShuffleMerge(object):

    def find_string(self):
        s = raw_input()
        counts = defaultdict(int)
        for x in s:
            counts[x] = counts[x] + 1
        l = counts.keys()
        l.sort()
        orig_s = ""
        for i in l:
            for j in range(counts.get(i)/2):
                orig_s += i
        while True:
            if
        print orig_s


ReverseShuffleMerge().find_string()
