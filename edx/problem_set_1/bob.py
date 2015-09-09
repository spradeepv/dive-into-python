s = raw_input()
find = 'bob'
count = 0
index = 0
while index < len(s):
        index = s.find(find, index)
        if index == -1:
            break
        index += 2
        count += 1
print "Number of times bob occurs is:", count