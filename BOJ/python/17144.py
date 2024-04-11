R, C, T = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maps = []
cacheMaps = [[0 for _ in range(C)] for _ in range(R)]
flag = True
top = 1
bottom = 2

for idx in range(R):
    row = list(map(int, input().split()))
    maps.append(row)
    if flag and row[0] == -1:
        top = idx
        bottom = idx + 1
        flag = False
    

def dust():
    for x in range(R):
        for y in range(C):
            count = 0
            d = maps[x][y]
            if d > 0:
                for idx in range(4):
                    nx = dx[idx] + x
                    ny = dy[idx] + y
                    if nx < 0 or ny < 0 or nx >= R or ny >= C:
                        continue
                    if maps[nx][ny] == -1:
                        continue

                    count += 1
                    cacheMaps[nx][ny] += d // 5

                cacheMaps[x][y] += maps[x][y] - ((d // 5) * count)
            
            elif d == -1:
                cacheMaps[x][y] = -1

    return cacheMaps

def cleanUp():
    value = maps[top][-1]
    maps[top][1:] = [0] + maps[top][1:-1]
    
    for idx in range(top - 1, -1, -1):
        value, maps[idx][-1] = maps[idx][-1], value

    value2 = maps[0][0]
    maps[0][:-1] = maps[0][1:-1] + [value]
    value = value2

    for idx in range(1, top):
        value, maps[idx][0] = maps[idx][0], value

def cleanDown():
    value = maps[bottom][-1]
    maps[bottom][1:] = [0] + maps[bottom][1:-1]

    for idx in range(bottom + 1, R):
        value, maps[idx][-1] = maps[idx][-1], value
    
    value2 = maps[R - 1][0]
    maps[R - 1][:-1] = maps[R - 1][1:-1] + [value]
    value = value2

    for idx in range(R - 2, bottom, -1):
        value, maps[idx][0] = maps[idx][0], value

for _ in range(T):
    # 미세먼지 확산
    maps = dust()

    cacheMaps = [[0 for _ in range(C)] for _ in range(R)]
    # 공기청정기 작동
    cleanUp()
    cleanDown()

answer = 0

for x in range(R):
    for y in range(C):
        answer += maps[x][y]

print(answer + 2)