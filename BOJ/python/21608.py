dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def func(favoite):
    
    # 초기화 - 이미 값이 있는지 여부 확인
    emptySpace = []

    for i in range(N):
        for j in range(N):
            if maps[i][j] == -1:
                emptySpace.append((i, j))

    # 1번
    cache = []
    maxValue = -1
    for i, j in emptySpace:
        count = 0
        for idx in range(4):
            nx = dx[idx] + i
            ny = dy[idx] + j

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if maps[nx][ny] in favoite: # 1번 조건
                count += 1

        if count > maxValue:    # 1번 처리
            cache = []
            maxValue = count
            cache.append((i, j))
        elif count == maxValue:
            cache.append((i, j))

    if len(cache) == 1:
        return cache[0]
    
    # 2번
    cache2 = []
    maxValue2 = -1
    for i, j in cache:
        count2 = 0
        for idx in range(4):
            nx = dx[idx] + i
            ny = dy[idx] + j

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if maps[nx][ny] == -1:  # 2번조건
                count2 += 1

        if count2 > maxValue2:  # 2번 처리
            cache2 = []
            maxValue2 = count2
            cache2.append((i, j))
        elif count == maxValue2:
            cache2.append((i, j))

    return cache2[0]

N = int(input())

maps = [[-1 for _ in range(N)] for __ in range(N)]

favoite = dict()

for i in range(N * N):
    a, b, c, d, e = list(map(int, input().split()))
    favoite[a] = [b, c, d, e]
    i, j = func(favoite[a])
    maps[i][j] = a

answer = 0

for i in range(N):
    for j in range(N):
        count = 0
        for idx in range(4):
            nx = dx[idx] + i
            ny = dy[idx] + j

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if maps[nx][ny] in favoite[maps[i][j]]:
                count += 1
        
        if count == 0:
            continue

        answer += 10 ** (count - 1)

print(answer)