def is_in_snakes(start, snakes, count):
    new_start = start
    if new_start in snakes:
        new_start -= 1
        count += 1
        if count >= 6:
            return True
        return is_in_snakes(new_start, snakes, count)
    else:
        return False


def get_count_to_position(start, end, count, snakes):
    print start, end, count, snakes
    diff = end - start
    #print "get_count_to_position : ", start, end, count
    if start == end:
        return count
    if diff == 6 or diff == 5 or diff == 4 or diff == 3 or diff == 2 or diff == 1:
        count += 1
        start += diff
        return get_count_to_position(start, end, count, snakes)
    elif diff > 6:
        new_start = start + 6
        if not is_in_snakes(start + 6, snakes, 1):
            count += 1
            start += 6
            return get_count_to_position(start, end, count, snakes)
        else:
            return None


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    ladder = {}
    for j in range(n):
        start, end = raw_input().split()
        start = int(start)
        end = int(end)
        ladder.update({end: start})
    m = int(raw_input())
    snake = {}
    for j in range(m):
        start, end = raw_input().split()
        start = int(start)
        end = int(end)
        snake.update({start: end})
    print ladder
    print snake
    l_keys = ladder.keys()
    l_values = ladder.values()
    s_keys = snake.keys()
    s_values = snake.values()
    l_keys.sort()
    l_keys.reverse()
    print l_keys
    count = 0
    start = 1
    print "l_keys >>>> ", l_keys
    print "l_values >>>> ", l_values
    print "s_keys >>>> ", s_keys
    print "s_values >>>> ", s_values

    for end_l in l_keys:
        if end_l not in snake.keys():
            start_l = ladder.get(end_l)
            count = get_count_to_position(start, start_l, count, snake.keys())
            print count
            if count is None:
                count = -1
                break
            else:
                start = end_l
                end = 100
                #print count
                count = get_count_to_position(start, end, count, snake.keys())
                if count:
                    break
                else:
                    continue
    if count is None:
        print -1
    else:
        print count