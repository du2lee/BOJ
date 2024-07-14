from collections import deque

N = 7

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()

q.append((0, 0, 0))

while q:
    x, y, d = q.popleft()

    for idx in range(4):
        nx = dx[idx] + x
        ny = dy[idx] + y

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if graph[nx][ny] != 0:
            continue

        graph[nx][ny] = d + 1
        q.append((nx, ny, d + 1))

if graph[N - 1][N - 1] == 0:
    print(-1)
else:
    print(graph[N - 1][N - 1])
    