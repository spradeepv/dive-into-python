s = raw_input()
count = 0
for c in s:
    if c in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print "Number of vowels:", count
