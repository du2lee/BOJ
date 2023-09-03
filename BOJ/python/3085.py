N = int(input())

maps = []
result = 0

dx = [1, 0]
dy = [0, 1]

for _ in range(N):
    cache = input()
    arr = []
    for j in cache:
        arr.append(j)
    maps.append(arr)

# 전체 체크
for i in range(N):
    for j in range(N):
        horizon = 1
        vertical = 1
        for k in range(i + 1, N):
            if maps[i][j] != maps[k][j]:
                break
            vertical += 1
        
        for k in range(j + 1, N):
            if maps[i][j] != maps[i][k]:
                break
            horizon += 1
        cache = max(vertical, horizon)
        if result < cache:
            result = cache

# 스위치 후 해당 라인 체크
for i in range(N):
    for j in range(N):
        for idx in range(2):
            nx = dx[idx] + i
            ny = dy[idx] + j

            if nx >= N or ny >= N:
                continue

            if maps[i][j] == maps[nx][ny]:
                continue

            cookie = maps[i][j]
            maps[i][j] = maps[nx][ny]
            maps[nx][ny] = cookie

            horizon = 1
            vertical = 1
            for x in range(i - 1, -1, -1):
                if maps[i][j] != maps[x][j]:
                    break
                vertical += 1
            for x in range(i + 1, N):
                if maps[i][j] != maps[x][j]:
                    break
                vertical += 1
            for y in range(j - 1, -1, -1):
                if maps[i][j] != maps[i][y]:
                    break
                horizon += 1
            for y in range(j + 1, N):
                if maps[i][j] != maps[i][y]:
                    break
                horizon += 1

            cache1 = max(horizon, vertical)

            horizon = 1
            vertical = 1
            for x in range(nx -1, -1, -1):
                if maps[nx][ny] != maps[x][ny]:
                    break
                vertical += 1
            for x in range(nx + 1, N):
                if maps[nx][ny] != maps[x][ny]:
                    break
                vertical += 1
            for y in range(ny - 1, -1, -1):
                if maps[nx][ny] != maps[nx][y]:
                    break
                horizon += 1
            for y in range(ny + 1, N):
                if maps[nx][ny] != maps[nx][y]:
                    break
                horizon += 1

            cache2 = max(horizon, vertical)
            cache = max(cache1, cache2)
            if result < cache:
                result = cache

            cookie = maps[i][j]
            maps[i][j] = maps[nx][ny]
            maps[nx][ny] = cookie

print(result)