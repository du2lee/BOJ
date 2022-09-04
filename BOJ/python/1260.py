from collections import deque

N, M, V = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
visited_bfs = [False for _ in range(N + 1)]
visited_dfs = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)




# import sys

# def bfs(graph, start_node):
#     visited, need_visit = list(), list()

#     need_visit.append(start_node)

#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])

#     return visited

# def dfs(graph, start_node):
#     visited, need_visit = list(), list()

#     need_visit.append(start_node)

#     while need_visit:
#         node = need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])

#     return visited



# Node, Edge, start_index = map(int, sys.stdin.readline().split())
# graph = dict()
# for node in range(1, Node + 1):                             #make key
#     graph[node] = []
# for _ in range(Edge):                                       #input Edge
#     A, B = map(int, sys.stdin.readline().split())
#     graph[A].append(B)
#     graph[B].append(A)



# for node in range(1,Node + 1):
#     graph[node].sort(reverse = True)
# array_dfs = dfs(graph, start_index)
# for node in range(1,Node + 1):
#     graph[node].sort()
# array_bfs = bfs(graph, start_index)


# for node in array_dfs:
#     print(node, end = ' ')
# print('')
# for node in array_bfs:
#     print(node, end = ' ')
# print('')