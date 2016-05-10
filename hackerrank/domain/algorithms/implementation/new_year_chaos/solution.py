T = int(raw_input().strip())
for a0 in range(T):
    n = int(raw_input().strip())
    q = [int(q_temp) for q_temp in raw_input().strip().split(' ')]
    # your code goes here
    a = [0] * (n + 1)
    chaos = False
    stop = False
    bribes = 0
    while not stop:
        stop = True
        for i in range(n-1):
            if q[i] > q[i+1]:
                a[q[i]] += 1
                #print a
                if a[q[i]] > 2:
                    stop = True
                    chaos = True
                    break
                bribes += 1
                q[i], q[i+1] = q[i+1], q[i]
                stop = False
    if chaos:
        print "Too chaotic"
    else:
        print bribes

