from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(checkMaps, x, y, blocks, color):

    # 방문 여부 표시
    checkMaps[x][y] = False

    # 블록 추가
    blocks.append((x, y))

    # 컬러 설정
    if color == 0:
        color = maps[x][y]

    # 인접 부분 확인
    for idx in range(4):
        nx = dx[idx] + x
        ny = dy[idx] + y

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if checkMaps[nx][ny] and maps[nx][ny] != -1 and maps[nx][ny] != -2 and (maps[nx][ny] == color or maps[nx][ny] == 0):
            dfs(checkMaps , nx, ny, blocks, color)

    if color == 0:  # 무지개 색만 있을 겨우
        return []

    return blocks

def gravity(y):
    bottom = N

    for idx in range(N - 1, -1, -1):
        a = maps[idx][y]

        if a == -1:
            bottom = idx
            continue

        if a != -2:
            if idx != bottom - 1:
                maps[bottom - 1][y] = maps[idx][y]
                maps[idx][y] = -2
                bottom -= 1
            else:
                bottom = idx

def rotate(maps):

    empty = []

    for row in zip(*maps):
        empty.append(list(row))

    maps = []

    for idx in range(N - 1, -1, -1):
        maps.append(empty[idx])
        
    return maps

N, M = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(N)]

scores = 0

while True:
    flag = True

    # 블록 찾기
    blocks = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == -1 or maps[i][j] == -2:
                continue

            checkMaps = [[True for __ in range(N)] for _ in range(N)]

            cache = dfs(checkMaps, i, j, [], maps[i][j])

            if len(cache) <= 1: # 블록 생성 조건 X
                continue

            if len(blocks) < len(cache):
                flag = False
                blocks = deepcopy(cache)
            elif len(blocks) == len(cache):
                # 무지개 갯수
                count1 = 0 
                count2 = 0
                x1 = -1
                y1 = -1
                x2 = -1
                y2 = -1

                blocks.sort()
                cache.sort()

                if blocks == cache:
                    continue

                for x, y in blocks:
                    if maps[x][y] == 0:
                        count1 += 1
                    elif x1 == -1 and y1 == -1 and maps[x][y] != -1 and maps[x][y] != -2:
                        x1 = x
                        y1 = y

                for x, y in cache:
                    if maps[x][y] == 0:
                        count2 += 1
                    elif x2 == -1 and y2 == -1 and maps[x][y] != -1 and maps[x][y] != -2:
                        x2 = x
                        y2 = y
                
                if count1 > count2:
                    continue

                if count1 < count2:
                    flag = False
                    blocks = deepcopy(cache)
                    
                # 기준 블록 행, 열이 큰 것
                if x1 < x2:
                    flag = False
                    blocks = deepcopy(cache)
                elif x1 == x2 and y1 < y2:
                    flag = False
                    blocks = deepcopy(cache)
           
    if flag:
        break

    # 점수 획득
    a = len(blocks)
    scores += a ** 2

    for x, y in blocks:
        maps[x][y] = -2

    # 중력 작용
    for i in range(N):
        gravity(i)

    # 90도 반시계
    cache2 = rotate(maps)
    maps = []
    maps = deepcopy(cache2)

    # 중력 작용
    for i in range(N):
        gravity(i)

print(scores)