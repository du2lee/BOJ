from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, X, Y, scale):
    q = deque([(X, Y, 0)])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[X][Y] = 0
    fishes = []

    while q:
        x, y, distance = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if  graph[nx][ny] > scale:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = distance + 1
                q.append((nx, ny, distance + 1))
                if 0 < graph[nx][ny] < scale:
                    fishes.append((visited[nx][ny], nx, ny))

    if len(fishes) == 0:
        return (-1, -1 ,-1)
    else:
        fishes.sort()           
        return fishes[0]

# search shark
shark = ()
scale = 2
exp = 0
time = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = (i, j)

while True:

    result = bfs(graph, shark[0], shark[1], scale)

    if result == (-1, -1 ,-1):
        print(time)
        break

    time += result[0]

    graph[shark[0]][shark[1]] = 0
    graph[result[1]][result[2]] = 9
    shark = result[1:]
    exp += 1

    if exp >= scale:
        scale += 1
        exp = 0