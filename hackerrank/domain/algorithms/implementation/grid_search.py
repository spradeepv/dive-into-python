class GridSearch(object):
    """

    """
    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

    def is_index_present(self, l1, l2):
        l = []
        if len(l1) == 0 and len(l2) > 0:
            l.extend(l2)
        for i in l1:
            for j in l2:
                if i == j:
                    l.append(i)
        return l

    def search(self):
        test_cases = int(raw_input())
        for i in range(test_cases):
            l = map(int, raw_input().split(' '))
            R, C = l[0], l[1]
            grid = [[raw_input()] for x in range(R)]
            l = map(int, raw_input().split(' '))
            r, c = l[0], l[1]
            grid_search = [[raw_input()] for x in range(r)]
            start = 0
            start_s = 0
            index = []
            found = False
            while True:
                if start >= R:
                    break
                for i in range(start_s, r):
                    if start >= R:
                        break
                    for j in range(start, R):
                        idx = list(self.find_all(grid[j][0], grid_search[i][0]))
                        if len(idx) > 0:
                            new_index = idx
                            if start != 0:
                                new_index = self.is_index_present(index, idx)
                            if len(new_index) != 0:
                                found = True
                                start_s = i + 1
                                start = j + 1
                                index = new_index
                                break
                            else:
                                start = j + 1
                                found = False
                                break
                        elif found:
                            found = False
                            start = j
                            break
                        else:
                            start = j + 1
                    if not found:
                        if i > 0:
                            start_s = i - 1
                        index = []
                        break
                if start_s >= r:
                    break
            print "YES" if found else "NO"

GridSearch().search()

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def check_policy_on_interface(policy_name, response):
    is_present = False
    if len(list(find_all(response, policy_name))) > 1:
        is_present = True
    return is_present



response = "SSH@NetIron MLX-4 Router#show access-list name net1 " \
           "SSH@NetIron MLX-4 Router#"
response_1 = "SSH@NetIron MLX-4 Router#show access-list name stdACL3 Standard IP access list stdACL3 permit any SSH@NetIron MLX-4 Router#"
#print check_policy_on_interface("net1", response)
#print check_policy_on_interface("stdACL3", response_1)