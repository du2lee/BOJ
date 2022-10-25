import copy
from collections import deque

N, M = list(map(int, input().split()))
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virus = [] # 바이러스 위치
empty = []
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            empty.append((i, j))
  
def bfs(graph):
    global result
    q = deque()
    for X, Y in virus:
        q.append((X, Y))
    
    while q:
        x, y = q.popleft()
        graph[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                
    cache = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                cache += 1
    if result < cache:
        result = cache

def makeWall(n):
    if n >= 3:
        graph2 = copy.deepcopy(graph)
        bfs(graph2)
        return

    for i, j in empty:
        if graph[i][j] == 0:
            graph[i][j] = 1
            makeWall(n + 1)
            graph[i][j] = 0

makeWall(0)

print(result)