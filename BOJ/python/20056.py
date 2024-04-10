from collections import deque

N, M, K = list(map(int, input().split()))

D = [(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1)]
maps = [[deque() for _ in range(N)] for __ in range(N)]
balls = deque()

def moveBalls(balls):
    cache = deque()

    while balls:
        r, c = balls.popleft()
        m, s, d = maps[r][c].popleft()
        dx = r + D[d][0] * s
        dy = c + D[d][1] * s

        # 범위 초과했을 때 처리
        if dx > N - 1:
            dx = dx % N
        elif dx < 0:
            dx = abs(dx % N)

        if dy > N - 1:
            dy = dy % N
        elif dy < 0:
            dy = abs(dy % N)

        maps[dx][dy].append((m, s, d))
        cache.append((dx, dy))
    
    return cache

def checks():
    cache = deque()

    for x in range(N):
        for y in range(N):
            l = len(maps[x][y])
            if l > 1:
                M = 0 # 질량
                S = 0 # 속력
                odd_count = 0
                while maps[x][y]:
                    m, s, d = maps[x][y].popleft()
                    M += m
                    S += s
                    if d % 2 == 1:
                        odd_count += 1

                M //= 5
                if M == 0:
                    continue
                S = S // l
                D1 = []

                if odd_count != l and odd_count != 0:
                    D1 = [1 ,3, 5, 7]
                else:
                    D1 = [0 ,2, 4, 6]
                
                for idx in D1:
                    maps[x][y].append((M, S, idx))
            
                for _ in range(4):
                    cache.append((x, y))
            elif l == 1:
                cache.append((x, y))
    return cache
                        

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    maps[r - 1][c - 1].append((m, s, d))
    balls.append((r - 1, c - 1))

for _ in range(K):
    # 파이어볼 이동시키기
    balls = moveBalls(balls)

    # 겹치는거 처리
    balls = checks()

answer = 0

for x, y in balls:
    m, s, d = maps[x][y].popleft()
    answer += m

print(answer)