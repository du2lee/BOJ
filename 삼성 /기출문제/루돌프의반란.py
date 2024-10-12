def in_board(x, y, N):
    return x >= 1 and y >= 1 and x <= N and y <= N

N, M, P, C, D = list(map(int, input().split()))

board = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
is_life = [True for _ in range(P+1)]
stun = [0 for _ in range(P+1)]
scores = [0 for _ in range(P+1)]
SantaX = [0 for _ in range(P+1)]
SantaY = [0 for _ in range(P+1)]

rodolf = list(map(int, input().split()))
board[rodolf[0]][rodolf[1]] = -1

for _ in range(P):
    id, x, y = tuple(map(int, input().split()))
    board[x][y] = id
    SantaX[id], SantaY[id] = x, y

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for T in range(1, M + 1):
    # 루돌프와 산타중 가장 가까운 곳 찾기
    closeX, closeY, closeD = 0, 0, 100000
    closeSanta = -1

    # 산타s 조회
    for id in range(1, P + 1):
        if not is_life[id]:
            continue

        cache = (rodolf[0]-SantaX[id])**2 + (rodolf[1]-SantaY[id])**2

        if closeD > cache:
            closeX, closeY, closeD = SantaX[id], SantaY[id], cache
            closeSanta = id
        elif closeD == cache:
            if closeX < SantaX[id]:
                closeX, closeY, closeD = SantaX[id], SantaY[id], cache
                closeSanta = id
            elif closeX == SantaX[id]:
                if closeY < SantaY[id]:
                    closeX, closeY, closeD = SantaX[id], SantaY[id], cache
                    closeSanta = id

    # 루돌프 돌진
    if closeSanta != -1:
        moveX, moveY = 0, 0
        board[rodolf[0]][rodolf[1]] = 0

        if rodolf[0] < closeX:
            moveX = 1
        elif rodolf[0] > closeX:
            moveX = -1
        
        if rodolf[1] < closeY:
            moveY = 1
        elif rodolf[1] > closeY:
            moveY = -1

        rodolf[0] += moveX
        rodolf[1] += moveY

    # 충돌 여부 확인
    if rodolf[0] == closeX and rodolf[1] == closeY:
        stun[closeSanta] = T + 1

        firstX, firstY = closeX + C*moveX, closeY + C*moveY
        lastX, lastY = firstX, firstY

        # 연쇄작용 적용
        while in_board(lastX, lastY, N) and board[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        while not (lastX == firstX and lastY == firstY):
            beforeX, beforeY = lastX - moveX, lastY - moveY

            if not in_board(beforeX, beforeY, N):
                break

            idx = board[beforeX][beforeY]
            if not in_board(lastX,lastY,N):
                is_life[idx] = False
            else:
                board[lastX][lastY] = idx
                SantaX[idx], SantaY[idx] = lastX, lastY

            lastX, lastY = beforeX, beforeY

        # 충돌 일어난 산타 처리
        scores[closeSanta] += C
        idx = board[closeX][closeY]
        if in_board(firstX, firstY, N):
            board[firstX][firstY] = idx
            SantaX[idx], SantaY[idx] = firstX, firstY
        else:
            is_life[idx] = False

    board[rodolf[0]][rodolf[1]] = -1

    # 산타 처리
    for id in range(1, P + 1):
        if not is_life[id]: # 아웃 산타
            continue
        if stun[id]>= T: # 기절 상태
            continue

        cache = (rodolf[0]-SantaX[id])**2 + (rodolf[1]-SantaY[id])**2
        moveX, moveY = 0, 0

        for dist in range(4):
            nx, ny = SantaX[id] + dx[dist], SantaY[id] + dy[dist]

            if not in_board(nx, ny, N):
                continue
            
            if board[nx][ny] > 0:
                continue

            cache2 = (rodolf[0]-nx)**2 + (rodolf[1]-ny)**2

            if cache2 < cache:
                cache = cache2
                moveX, moveY = dx[dist], dy[dist]

        # 산타 이동
        if moveX or moveY:
            board[SantaX[id]][SantaY[id]] = 0
            a = SantaX[id] + moveX
            b = SantaY[id] + moveY

            # 충돌 했을 때
            if rodolf[0] == a and rodolf[1] == b:
                stun[id] = T + 1

                firstX, firstY = a - D * moveX, b - D * moveY
                lastX, lastY = firstX, firstY

                while in_board(lastX, lastY, N) and board[lastX][lastY] > 0:
                    lastX -= moveX
                    lastY -= moveY

                while not (lastX == firstX and lastY == firstY):
                    beforeX, beforeY = lastX + moveX, lastY+ moveY

                    if not in_board(beforeX, beforeY, N):
                        break

                    idx = board[beforeX][beforeY]

                    if in_board(lastX, lastY, N):
                        board[lastX][lastY] = idx
                        SantaX[idx], SantaY[idx] = lastX, lastY
                    else:
                        is_life[idx] = False

                    lastX, lastY = beforeX, beforeY

                scores[id] += D
                SantaX[id], SantaY[id] = firstX, firstY

                if in_board(firstX, firstY, N):
                    board[firstX][firstY] = id
                else:
                    is_life[id] = False
            
            else:
                board[a][b] = id
                SantaX[id], SantaY[id] = a, b

    for id in range(1, P + 1):
        if is_life[id]:
            scores[id] += 1

for id in range(1, P + 1):
    print(scores[id] ,end = " ")