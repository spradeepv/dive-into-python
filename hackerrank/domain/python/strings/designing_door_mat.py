n, m = map(int, raw_input().split())
middle = n/2
_width = n/3
HYPHEN = "-"
DOT = ".|."
WELCOME = "WELCOME"
dot_width = 1
for i in range(n):
    if i < middle:
        print (HYPHEN*(3*(_width+1))).ljust((3*(_width+1)))+ (DOT * dot_width) + (HYPHEN*(3*(_width+1)))
        _width -=1
        dot_width += 2
    elif i == 4:
        print (HYPHEN * ((m - len(WELCOME))/2)) + WELCOME + (HYPHEN * ((m - len(WELCOME))/2))
        _width += 1
        dot_width -= 2
    else:
        print (HYPHEN*(3*(_width+1))).ljust((3*(_width+1)))+ (DOT * dot_width) + (HYPHEN*(3*(_width+1)))
        _width +=1
        dot_width -= 2

N=n
M=m
for i in xrange(1,N,2):
    print ("-" * ((m - 3*i) / 2)) + (".|." * i) + ("-" * ((m - 3*i) / 2))
print ("-" * ((m - len("WELCOME"))/2)) + "WELCOME" + ("-" * ((m - len("WELCOME"))/2))
for i in xrange(N-2,-1,-2):
    print ("-" * ((m - 3*i) / 2)) + (".|." * i) + ("-" * ((m - 3*i) / 2))