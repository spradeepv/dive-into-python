"""
You are given a matrix with mm rows and nn columns of cells, each of which
contains either 11 or 00. Two cells are said to be connected if they are
adjacent to each other horizontally, vertically, or diagonally. The
connected and filled (i.e. cells that contain a 11) cells form a region.
There may be several regions in the matrix. Find the number of cells in the
largest region in the matrix.

Input Format
There will be three parts of t input:
The first line will contain mm, the number of rows in the matrix.
The second line will contain nn, the number of columns in the matrix.
This will be followed by the matrix grid: the list of numbers that make up
the matrix.

Output Format
Print the length of the largest region in the given matrix.

Constraints
0<m<100<m<10
0<n<100<n<10

Sample Input:

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output:

5
Task:
Write the complete program to find the number of cells in the largest region.

Explanation

X X 0 0
0 X X 0
0 0 X 0
1 0 0 0
The X characters indicate the largest connected component, as per the given
definition. There are five cells in this component.
"""
seen = {}
graph = {}
def dfs(node):
    seen[node] = True
    for next in graph[node]:
        if not seen[next]:
            dfs(next)


m = int(raw_input())
n = int(raw_input())
a = [[0 for x in range(m)] for j in range(n)]
for i in range(m):
    l = map(int, raw_input().split())
    for j in range(n):
        a[i][j] = l[j]
print a
for i in range(m):
    for j in range(n):
        pass


