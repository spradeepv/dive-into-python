"""
Problem Statement

Given an undirected graph consisting of N nodes (labelled 1 to N) where a
specific given node S represents the start position and an edge between any
two nodes is of length 6 units in the graph.

It is required to calculate the shortest distance from start position (Node
S) to all of the other nodes in the graph.

Note 1: If a node is unreachable, the distance is assumed as -1.
Note 2: The length of each edge in the graph is 6 units.

Input Format

The first line contains T, denoting the number of test cases.
First line of each test case has two integers N, denoting the number of
nodes in the graph and M, denoting the number of edges in the graph.
The next M lines each consist of two space separated integers x y, where x
and y denote the two nodes between which the edge exists.
The last line of a testcase has an integer S, denoting the starting position.

Constraints
1<=T<=10
2<=N<=1000
1<=M<=N*(N-1)2
1<=x,y,S<=N

Output Format

For each of T test cases, print a single line consisting of N-1
space-separated integers, denoting the shortest distances of the N-1 nodes
from starting position S. This will be done for all nodes same as in the
order of input 1 to N.

For unreachable nodes, print -1.

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

For test cases 1:

S denotes the node 1 in the test case and B,C and D denote 2,3 and 4. Since
S is the starting node and the shortest distances from it are (1 edge,
1 edge, Infinity) to the nodes B,C and D (2,3 and 4) respectively.

Node D is unreachable, hence -1 is printed (not Infinity).

For test cases 2: There are only one edge (2, 3) in a graph with 3 nodes,
so node 1 is unreachable from node 2, and node 3 has one edge from node 2,
each edge has the length of 6 units. So we output -1 6.
"""


class Graph(object):
    """
    Simple graph
    """

    def __init__(self, graph_dict=None):
        self._graph_dict = {}
        if graph_dict:
            self._graph_dict = graph_dict

    def vertices(self):
        """Returns the vertices of the graph"""
        return list(self._graph_dict.keys())

    def edges(self):
        """Returns the edges of the graph"""
        return self._generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ Assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self._graph_dict and vertex2 in self._graph_dict:
            if vertex2 not in self._graph_dict[vertex1]:
                self._graph_dict[vertex1].append(vertex2)
            if vertex1 not in self._graph_dict[vertex2]:
                self._graph_dict[vertex2].append(vertex1)
        elif vertex1 in self._graph_dict:
            if vertex2 not in self._graph_dict[vertex1]:
                self._graph_dict[vertex1].append(vertex2)
        elif vertex2 in self._graph_dict:
            if vertex1 not in self._graph_dict[vertex2]:
                self._graph_dict[vertex2].append(vertex1)
        else:
            self._graph_dict[vertex1] = [vertex2]
            self._graph_dict[vertex2] = [vertex1]

    def find_path(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in self._graph_dict:
            return None
        if end_vertex in self._graph_dict[start_vertex]:
            path = path + [end_vertex]
            return path
        for vertex in self._graph_dict[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self._graph_dict:
            return []
        paths = []
        if end_vertex in self._graph_dict[start_vertex]:
            path = path + [end_vertex]
            paths.append(path)
            return paths
        for vertex in self._graph_dict[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def bfs(self, start):
        graph = self._graph_dict
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited

    def bfs_paths(self, start, end):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in list(set(self._graph_dict[vertex]) - set(path)):
                if next == end:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def shortest_path(self, start, end):
        try:
            return next(self.bfs_paths(start, end))
        except StopIteration:
            return None

    def _generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbor in self._graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        return res

def solution():
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        #print n, m
        graph = Graph()
        for i in range(1, n+1):
            graph.add_vertex(i)
        for j in range(m):
            vertex1, vertex2 = map(int, raw_input().split())
            graph.add_edge([vertex1, vertex2])
        s = int(raw_input())
        for vertex in graph.vertices():
            if vertex != s:
                path = graph.shortest_path(s, vertex)
                if path:
                    print str((len(path) - 1) * 6),
                else:
                    print -1,
        print

if __name__ == '__main__':
    solution()
