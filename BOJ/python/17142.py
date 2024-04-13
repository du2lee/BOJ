from collections import deque
from copy import deepcopy
from math import inf

N, M = list(map(int, input().split()))

maps = []
virus = []
choice = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            virus.append((i, j))
    maps.append(row)

def combinations(n, newArr, c):
    if len(newArr) == n:
        choice.append(deque(newArr))
        return
    for i in range(c, len(virus)):
        combinations(n, newArr + [virus[i]], i + 1)

combinations(M, [], 0)

answer = -1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q, graphs):
    timeGraph = [[0 for _ in range(N)] for __ in range(N)]

    for x, y in q:
        graphs[x][y] = 3

    # 바이러스 퍼트리기
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graphs[nx][ny] == 1 or graphs[nx][ny] == 3: # 벽 and 이미 활성 
                continue
            
            graphs[nx][ny] = 3
            timeGraph[nx][ny] = timeGraph[x][y] + 1
            q.append((nx, ny))

    # 다 퍼졌는지 체크
    answer = 0

    for x in range(N):
        for y in range(N):
            if graphs[x][y] == 0:
                return -1
            if maps[x][y] != 2:
                answer = max(answer, timeGraph[x][y])

    return answer

answer = inf

for q in choice:
    copyMaps = deepcopy(maps)
    v = bfs(q, copyMaps)
    if v == -1:
        continue
    answer = min(v, answer)

if answer == inf:
    print(-1)
else:
    print(answer)