s = raw_input()
print any(c.isalpha() for c in s) or any(c.isdigit() for c in s)
print any(c.isalpha() for c in s)
print any(c.isdigit() for c in s)
print any(c.islower() for c in s)
print any(c.isupper() for c in s)
