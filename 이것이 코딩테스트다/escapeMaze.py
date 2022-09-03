from collections import deque

N, M = list(map(int, input().split()))

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque([[x, y]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x + dx[i] < 0 or N <= x + dx[i] or y + dy[i] < 0 or M <= y + dy[i]:
                continue

            if graph[x + dx[i]][y + dy[i]] == 0:
                continue
            
            if graph[x + dx[i]][y + dy[i]] == 1:
                graph[x + dx[i]][y + dy[i]] = graph[x][y] + 1
                queue.append([x + dx[i], y + dy[i]])
    print(graph[N - 1][M - 1])
        

bfs(0, 0)
