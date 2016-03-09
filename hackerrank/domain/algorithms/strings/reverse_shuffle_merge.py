class ReverseShuffleMerge(object):

    def small_lexi(self, s):
        letters = list(set(list(s)))
        letters.sort()
        reverse_s = s[::-1]
        counter = {i:(s.count(i))/2 for i in letters}
        print letters, reverse_s, counter
        A = ''
        for j in range(len(s)):
            if reverse_s[j:].count(reverse_s[j]) == counter[reverse_s[j]]:
                counter[reverse_s[j]] -= 1
                A += reverse_s[j]
            elif reverse_s[j] == letters[0]:
                if counter[letters[0]] > 0:
                    counter[letters[0]] -= 1
                    A += letters[0]
                else:
                    letters.pop(0)
            else:
                continue
        return A

print ReverseShuffleMerge().small_lexi(raw_input())
