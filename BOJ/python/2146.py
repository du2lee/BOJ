from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
island = []
dx = [1, -1, 0 ,0]
dy = [0, 0, -1, 1]
result = 2 * N

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] == 0
    land = []

    while queue:
        x, y = queue.popleft()
        land.append([x, y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0
    return land

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            island.append(bfs(i, j))

for i in range(len(island)):
    for j in range(i + 1, len(island)):
        for first in island[i]:
            for second in island[j]:
                x = abs(first[0] - second[0])
                y = abs(first[1] - second[1])
                if x + y < result:
                    result = x + y
print(result - 1)