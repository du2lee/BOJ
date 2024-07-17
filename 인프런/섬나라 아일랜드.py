from collections import deque

N = int(input())

graph = []
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]
answer = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(X, Y):
    q = deque()

    q.append((X, Y))

    while q:
        x, y = q.popleft()

        graph[x][y] = 0

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            bfs(x, y)
            answer += 1
                

print(answer)

