import sys

Node = int(sys.stdin.readline())
Edge = int(sys.stdin.readline())


def dfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

graph = dict()

for node in range(1, Node + 1):                                          #key
    graph[node] = []

for _ in range(Edge):                                                    #value
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

print(len(dfs(graph, 1)) - 1)