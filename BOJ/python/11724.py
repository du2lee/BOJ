N, M = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
count = 0

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for idx in range(1, N + 1):
    if not visited[idx]:
        dfs(idx)
        count += 1

print(count)
