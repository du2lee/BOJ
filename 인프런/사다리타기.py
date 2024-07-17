N = 10

graph = []
X = N - 1
Y = 0
dx = [0, 0, -1]
dy = [1, -1, 0]

for _ in range(N):
    graph.append(list(map(int, input().split())))

for y in range(N):
    if graph[N - 1][y] == 2:
        Y = y
        break

while True:

    for i in range(3):
        nx = dx[i] + X
        ny = dy[i] + Y

        if ny < 0 or ny >= N:
            continue

        if graph[nx][ny] == 0:
            continue

        graph[nx][ny] = 0
        X, Y = nx, ny
        break

    if X == 0:
        break

print(Y)