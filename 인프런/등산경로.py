from math import inf

N = int(input())

graph = []
check = []

start = inf
sx = 0
sy = 0
end = -1
ex = 0
ey = 0

# 그래프 그리기, 출발지, 도착지 찾기
for x in range(N):
    row = list(map(int, input().split()))
    for y in range(N):
        if start > row[y]:
            sx = x
            sy = y
            start = row[y]

        if end < row[y]:
            ex = x
            ey = y
            end = row[y]

    graph.append(row)
    check.append([False for _  in range(N)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

def dfs(x, y, check):
    global answer

    if x == ex and y == ey:
        answer += 1
        return

    check[x][y] = True

    for idx in range(4):
        nx = dx[idx] + x
        ny = dy[idx] + y

        if nx < 0 or ny < 0 or nx >=N or ny >= N:
            continue

        if check[nx][ny]:
            continue

        if graph[nx][ny] <= graph[x][y]:
            continue

        dfs(nx, ny, check)
    
    check[x][y] = False

dfs(sx, sy, check)

print(answer)