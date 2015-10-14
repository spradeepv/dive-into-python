# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
l = []
for i in range(n):
    commands = raw_input().split()
    count = 0
    method = ""
    method = commands[0]
    args = map(int, commands[1:])
    if method == "print":
        print l
    elif not args and method != "print":
        getattr(l, method)()
    elif len(args) == 1:
        getattr(l, method)(args[0])
    else:
        getattr(l, method)(args[0], args[1])

