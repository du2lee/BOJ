from collections import deque

N = int(input())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
counts = []

for _ in range(N):
    graph.append(list(input()))

def bfs(X, Y):
    q = deque()
    count = 0

    q.append((X, Y))
    graph[X][Y] = '0'

    while q:
        x, y = q.popleft()
        count += 1
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == '1':
                q.append((nx, ny))
                graph[nx][ny] = '0'
    
    return count

for x in range(N):
    for y in range(N):
        if graph[x][y] != '0':
            answer += 1
            counts.append(bfs(x, y))

print(answer)
counts.sort()
for v in counts:
    print(v)

