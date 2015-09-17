"""
Problem Statement
You are given a tree (a simple connected graph with no cycles). You have to remove as many edges from the tree as
possible to obtain a forest with the condition that : Each connected component of the forest should contain an even
number of vertices.
"""


def get_sum(num_of_nodes, vertices, cur, pi):
    if num_of_nodes[cur]==0:
        print vertices[cur]
        for nigh in vertices[cur]:
            print nigh, pi
            if nigh!=pi:
                num_of_nodes[cur] += get_sum(num_of_nodes, vertices, nigh, cur)
        num_of_nodes[cur] += 1  # itself

    return num_of_nodes[cur]

def solve(N, M, E):
    num_of_nodes = [0 for _ in xrange(N+1)]
    vertices = [[] for _ in xrange(N+1)]
    ele = []
    for e in E:
        u, v = e
        ele.append([u, v])
        vertices[u].append(v)
        vertices[v].append(u)
    print vertices
    print ele
    get_sum(num_of_nodes, vertices, 1, 0)
    print num_of_nodes
    result = 0
    for i in xrange(2, N+1):  # excluding root
        if num_of_nodes[i]%2==0:
            result += 1
    return result

N, M = map(int, raw_input().strip().split(' '))
E = []
for t in xrange(M):
    # construct cipher
    E.append(map(int, raw_input().strip().split(' ')))
print E
s = solve(N, M, E)
print s