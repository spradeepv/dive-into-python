"""

"""

for i in range(1,int(raw_input())+1):
    print "".join(map(str, [x if x<=i else x-i for x in range(1, i + (i-1)+1)]))