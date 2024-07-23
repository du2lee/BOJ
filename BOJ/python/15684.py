from copy import deepcopy

N, M, H = list(map(int, input().split()))

maps = [[-2 for _ in range(N + 2)] for __ in range(H + 2)]

for _ in range(M):
    x, y = list(map(int, input().split()))
    maps[x][y] = y + 1
    maps[x][y + 1] = y

answer = -1

def move(x, y, flag, maps):

    if maps[x][y] == y + 1 and flag:
        return x, y + 1, False
    if maps[x][y]== y - 1 and flag:
        return x, y - 1, False
    return x + 1, y, True

def draw(x, y, flag, maps):
    while x < H + 1:
        x, y, flag = move(x, y, flag, maps)
    return x, y, flag

def dfs(depth, xxx, yyy, maps):
    global answer
    if depth > 3:
        return 
    
    cacheMaps = deepcopy(maps)

    for i in range(xxx, H + 1):
        for j in range(yyy, N):
            if cacheMaps[i][j] != -2 or cacheMaps[i][j + 1] != -2 :
                continue

            cacheMaps[i][j] = j + 1
            cacheMaps[i][j + 1] = j

            flag = True
            flag2 = False
    
            # 그려보기
            for y in range(1, N + 1):
                nx, ny, a = draw(0, y, True, cacheMaps)
                if ny != y:
                    flag = False
                    break

            # 잘 나오면 answer = depth
            if flag:
                answer = depth
                return True
            else:
                if j == N - 1:
                    flag2 = dfs(depth + 1, i + 1, 1, cacheMaps)
                else:
                    flag2 = dfs(depth + 1, i, j + 1, cacheMaps)

            # 원상복구
            cacheMaps = deepcopy(maps)

            if flag2:
                return flag2
                   
# 0개 추가 했을 때
if M == 0:
    answer = 0
else:
    dfs(1, 1, 1, maps)    
print(answer)