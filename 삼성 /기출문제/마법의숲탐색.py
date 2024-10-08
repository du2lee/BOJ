X, Y, K = list(map(int, input().split()))
answer = 0

graph = [[0 for __ in range(Y)] for _ in range(X) ]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
dl = [(-1, 0), (0, 1), (1, 0), (0, -1)]

doors = [[0, 0] for _ in range(10000)]


def location(y, d):
    # 정령 위치
    x = -2

    while True:
        # 남
        if x == -2: # 처음 시작
            if graph[x + 2][y] == 0:
                x += 1
                continue
        else:
            if x + 2 < X: # 하단 체크
                if graph[x + 2][y] == 0 and graph[x + 1][y - 1] == 0 and graph[x + 1][y + 1] == 0:
                    x += 1
                    continue
        # 서
        if y - 2 >= 0 and x + 2 < X: # 가장자리 체크
            if x == -2:
                if graph[x+2][y-1] == 0:
                    x += 1
                    y -= 1
                    d -= 1
                    if d < 0:
                        d = 3
                    continue
            elif x == -1:
                if graph[x+1][y-1] == 0 and graph[x+1][y-2] == 0 and graph[x+2][y-1] == 0:
                    x += 1
                    y -= 1
                    d -= 1
                    if d < 0:
                        d = 3
                    continue
            elif x == 0:
                if graph[x][y-2] == 0 and graph[x+1][y-1] == 0 and graph[x+1][y-2] == 0 and graph[x+2][y-1] == 0:
                    x += 1
                    y -= 1
                    d -= 1
                    if d < 0:
                        d = 3
                    continue
            else:
                if graph[x][y-2] == 0 and graph[x-1][y-1] == 0 and graph[x+1][y-1] == 0 and graph[x+1][y-2] == 0 and graph[x+2][y-1] == 0:
                    x += 1
                    y -= 1
                    d -= 1
                    if d < 0:
                        d = 3
                    continue
        # 동
        if y + 2 < Y and x + 2 < X: # 가장자리 체크
            if x == -2:
                if graph[x+2][y+1] == 0:
                    x += 1
                    y += 1
                    d += 1
                    if d > 3:
                        d = 0
                    continue
            elif x == -1:
                if graph[x+1][y+1] == 0 and graph[x+1][y+2] == 0 and graph[x+2][y+1] == 0:
                    x += 1
                    y += 1
                    d += 1
                    if d > 3:
                        d = 0
                    continue
            elif x == 0:
                if graph[x][y+2] == 0 and graph[x+1][y+1] == 0 and graph[x+1][y+2] == 0 and graph[x+2][y+1] == 0:
                    x += 1
                    y += 1
                    d += 1
                    if d > 3:
                        d = 0
                    continue
            else:
                if graph[x][y+2] == 0 and graph[x-1][y+1] == 0 and graph[x+1][y+1] == 0 and graph[x+1][y+2] == 0 and graph[x+2][y+1] == 0:
                    x += 1
                    y += 1
                    d += 1
                    if d > 3:
                        d = 0
                    continue
        break
    return x, y, d

ddx = [0, 0, 1, -1]
ddy = [1, -1, 0, 0]
checkGraph = [[0 for __ in range(Y)] for _ in range(X)]

def dfs(x, y, n, checkGraph):
    checkGraph[x][y] = 1

    for idx in range(4):
        nx = x + ddx[idx]
        ny = y + ddy[idx]

        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
            continue

        if graph[nx][ny] == 0:
            continue

        if graph[x][y] != graph[nx][ny]:
            ax, ay = doors[graph[x][y]]
            if x != ax or y != ay:
                continue

        if checkGraph[nx][ny] != 0:
            continue

        n = max(n, nx) 
        n = max(n, dfs(nx, ny, n, checkGraph))

    return n


for idx in range(1, K + 1):
    c, d = list(map(int, input().split()))


    # 위치 배치
    x, y, o = location(c - 1, d)

    if x < 1:
        graph = [[0 for __ in range(Y)] for _ in range(X) ]
        continue
    else:
        for i in range(5):
            graph[x+dx[i]][y+dy[i]] = idx
        a, b = dl[o]
        doors[idx] = [x + a, y + b]
    # 점수 계산 
    checkGraph = [[0 for __ in range(Y)] for _ in range(X)]
    answer += (dfs(x, y, x, checkGraph) + 1)

print(answer)
