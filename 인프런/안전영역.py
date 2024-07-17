from collections import deque
from copy import deepcopy

N = int(input())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(X, Y, h, graph):
    q = deque()

    q.append((X, Y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] > h:
                q.append((nx, ny))
                graph[nx][ny] = 0

    return graph

answer = 0

for h in range(1, 100):
    count = 0
    cache = deepcopy(graph)

    for x in range(N):
        for y in range(N):
            if cache[x][y] > h:
                count += 1
                cache = bfs(x, y, h, cache)

    answer = max(answer, count)

print(answer)