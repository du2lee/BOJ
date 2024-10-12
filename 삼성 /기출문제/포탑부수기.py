from collections import deque

N, M, K = list(map(int, input().split()))

board = [[0 for _ in range(M + 1)]]
attack_time = [[0 for _ in range(M + 1)] for __ in range(N + 1)]
repair = [[True for _ in range(M + 1)] for __ in range(N + 1)]

for _ in range(N):
    board.append([0] + list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ddx = [-1, -1, -1, 0, 0, 1, 1, 1]
ddy = [-1, 0, 1, -1, 1, -1, 0, 1]

def func(sx, sy, ex, ey): # 레이저 공격
    q = deque()
    q.append([sx,sy,[(sx,sy)]])
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    visited[sx][sy] = True

    while q:
        x, y, route = q.popleft()
        visited[x][y] = True

        if x == ex and y == ey:
            return True, route
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx == 0: nx = N
            if nx == N + 1: nx = 1
            if ny == 0: ny = M
            if ny == M + 1: ny = 1

            if visited[nx][ny] or board[nx][ny] == 0:
                continue

            q.append([nx, ny, route + [(nx, ny)]])
    
    return False, []


for T in range(1, K + 1):
    max_score, min_score = 0, 5001
    attacker = (0, 0)
    defender = (0, 0)

    repair = [[True for _ in range(M + 1)] for __ in range(N + 1)]

    # 남은 포탑 갯수
    left_towel = 0

    for x in range(1, N + 1):
        for y in range(1, M + 1):
            # 부러진 포탑 생략
            if board[x][y] == 0:
                continue
            
            left_towel += 1

            # 공격자 선정
            if min_score > board[x][y]:
                min_score = board[x][y]
                attacker = (x, y)
            elif min_score == board[x][y]:
                if attack_time[attacker[0]][attacker[1]] < attack_time[x][y]:
                    attacker = (x, y)
                elif attack_time[attacker[0]][attacker[1]] == attack_time[x][y]:
                    if attacker[0] + attacker[1] < x + y:
                        attacker = (x, y)
                    elif attacker[0] + attacker[1] == x + y:
                        if attacker[1] < y:
                            attacker = (x, y)

            # 방어자 선정
            if max_score < board[x][y]:
                max_score = board[x][y]
                defender = (x, y)
            elif max_score == board[x][y]:
                if attack_time[defender[0]][defender[1]] > attack_time[x][y]:
                    defender = (x, y)
                elif attack_time[defender[0]][defender[1]] == attack_time[x][y]:
                    if defender[0] + defender[1] > x + y:
                        defender = (x, y)
                    elif defender[0] + defender[1] == x + y:
                        if defender[1] > y:
                            defender = (x, y)

    if left_towel <= 1:
        break
            
    attack_time[attacker[0]][attacker[1]] = T
    board[attacker[0]][attacker[1]] += N+M

    repair[attacker[0]][attacker[1]] = False
    repair[defender[0]][defender[1]] = False

    if attacker == defender:
        continue
    
    flag, route = func(attacker[0], attacker[1], defender[0], defender[1])
    
    # 레이저 공격
    if flag:
        for x, y in route[1:-1]:
            board[x][y] -= board[attacker[0]][attacker[1]] // 2
            repair[x][y] = False
    # 포탄 공격
    else:
        for d in range(8):
            nx, ny = defender[0] + ddx[d], defender[1] + ddy[d]
            if nx == 0: nx = N
            if nx == N + 1: nx = 1
            if ny == 0: ny = M
            if ny == M + 1: ny = 1

            if nx == attacker[0] and ny == attacker[1]:
                continue

            repair[nx][ny] = False
            board[nx][ny] -= board[attacker[0]][attacker[1]] // 2

    board[defender[0]][defender[1]] -= board[attacker[0]][attacker[1]] 

    # 포탑 부서짐 및 정비
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if board[x][y] <= 0:
                board[x][y] = 0
            else:
                if repair[x][y]:
                    board[x][y] += 1

answer = 0

for row in board:
    answer = max(answer, max(row))

print(answer)