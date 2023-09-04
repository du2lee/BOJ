N, M, B = list(map(int, input().split()))

maps = []
maxHeight = -1
result = [int(10e9), -1] 

for _ in range(N):
    cache = list(map(int, input().split()))
    maps.append(cache)
    maxHeight = max(max(cache), maxHeight)

for floor in range(maxHeight + 1):
    cache = 0
    useBlock = 0
    for x in range(N):
        for y in range(M):
            if maps[x][y] < floor:
                cache += (floor - maps[x][y])
                useBlock += (floor - maps[x][y])
            else:
                cache += ((maps[x][y] - floor) * 2)
                useBlock -= (maps[x][y] - floor)
    if useBlock > B:
        break
    if result[0] >= cache:
        result[0] = cache
        result[1] = floor

print(result[0], result[1])