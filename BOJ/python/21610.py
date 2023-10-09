def up(x, s, N):
    cache = s % N
    x -= cache
    if x < 0:
        x += N
    return x

def down(x, s, N):
    cache = s % N
    x += cache
    if x >= N:
        x -= N
    return x

def move(x, y, d, s, N):
    if d == 1:
        y = up(y, s, N)
    elif d == 2:
        y = up(y, s, N)
        x = up(x, s, N)
    elif d == 3:
        x = up(x, s, N)
    elif d == 4:
        x = up(x, s, N)
        y = down(y, s, N)
    elif d == 5:
        y = down(y, s, N)
    elif d == 6:
        y = down(y, s, N)
        x = down(x, s, N)
    elif d == 7:
        x = down(x, s, N)
    elif d == 8:
        x = down(x, s, N)
        y = up(y, s, N)
    return x, y

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

def checkClouds(x, y, N):
    count = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if maps[nx][ny] > 0:
            count += 1
    return count

N, M = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for d, s in moves:
    checkMap = [[True for _ in range(N)] for _ in range(N)]
    # 구름 이동 및 + 1
    for idx in range(len(clouds)):
        x, y = clouds[idx]
        x, y = move(x, y, d, s, N)
        maps[x][y] += 1
        clouds[idx] = [x, y]
    # 구름 체크 및 대각선 플러스 구름삭제
    for x, y in clouds:
        maps[x][y] += checkClouds(x, y, N)
        checkMap[x][y] = False
    clouds = []
    # 나머지 구름 생성
    for x in range(N):
        for y in range(N):
            if maps[x][y] >= 2 and checkMap[x][y]:
                clouds.append([x, y])
                maps[x][y] -= 2

result = 0
for x in range(N):
    for y in range(N):
        result += maps[x][y]
print(result)