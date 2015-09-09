s = raw_input()
l = []
ascii_val = 97
temp_str = ''
i = 0
while i < len(s):
    c = s[i]
    curr_ascii_val = ord(c)
    if curr_ascii_val >= ascii_val:
        temp_str += c
        #ascii_val = curr_ascii_val
        i += 1
    else:
        l.append(temp_str)
        temp_str = ''
    ascii_val = curr_ascii_val
if not l or temp_str not in l:
    l.append(temp_str)
length = 0
result = ''
print l
for s in l:
    if len(s) > length:
        length = len(s)
        result = s
print "Longest substring in alphabetical order is:", result