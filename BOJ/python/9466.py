import sys

sys.setrecursionlimit(111111)

def dfs(v, result):
    visited[v] = True
    cycle.append(v)

    if visited[graph[v]]:
        if graph[v] in cycle:   # 사이클이 존재함.
            result += cycle[cycle.index(graph[v]):]
    else:
        dfs(graph[v], result)


T = int(input())

for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False for _ in range(N + 1)]
    result = []

    for i in range(1, N + 1):
        if not visited[i]:
            cycle = []
            dfs(i, result)

    print(N - len(result))