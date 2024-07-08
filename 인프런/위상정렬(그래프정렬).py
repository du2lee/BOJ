from collections import deque

N, M = list(map(int, input().split()))

degree = [0 for _ in range(N + 1)]
graph = [[0 for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(M):
    s, e = list(map(int, input().split()))
    degree[e] += 1
    graph[s][e] = 1

q = deque()

for idx in range(1, N + 1):
    if degree[idx] == 0:
        q.append(idx)
        degree[idx] -= 1

while q:
    node = q.popleft()
    print(node, end = " ")

    for idx in range(1, N + 1):
        if graph[node][idx] == 1:
            degree[idx] -= 1
            if degree[idx] == 0:
                q.append(idx)