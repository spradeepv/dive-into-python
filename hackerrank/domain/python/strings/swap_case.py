s = raw_input()
new_s = ""
for c in s:
    ascii_val = ord(c)
    if  ascii_val >= 65 and ascii_val <= 90:
        ascii_val += 32
    elif ascii_val >= 97 and ascii_val <= 122:
        ascii_val -= 32
    new_s += chr(ascii_val)
print new_s