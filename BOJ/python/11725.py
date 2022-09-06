import sys

sys.setrecursionlimit(111111)

N = int(input())

graph = [[] for _ in range(N + 1)]

parent = [0 for _ in range(N + 1)]
parent[1] = 1

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)
            
dfs(1)

for i in range(2, N + 1):
    print(parent[i])