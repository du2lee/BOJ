from collections import deque
T = int(input())

graph = []
visited = []

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for idx in graph[v]:
            if not visited[idx]:
                queue.append(idx)
                visited[idx] = True

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    count = 0

    for i in range(N):
        graph[i + 1].append(array[i])
        graph[array[i]].append(i + 1)
    
    for idx in range(1, N + 1):
        if not visited[idx]: 
            bfs(idx)
            count += 1
    print(count)