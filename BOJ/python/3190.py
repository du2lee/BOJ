from collections import deque

N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = list(map(int, input().split()))
    graph[x - 1][y - 1] = 1
L = int(input())
actions = []
for _ in range(L):
    x, y = input().split()
    actions.append((int(x), y))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0           # 방향
time = 0        # 시간
x, y  = 0, 0    # 위치
idx = 0         # check 위치
graph[x][y] = 2
snake = deque([(0,0)])

while True:
    time += 1
    # 앞으로 가
    x += dx[d]
    y += dy[d]

    # 벽 or 꼬리?
    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] == 2:
        print(time)
        break

    if not graph[x][y] == 1:                # 사과X
        nx, ny = snake.popleft()
        graph[nx][ny] = 0
    
    graph[x][y] = 2
    snake.append((x, y))

    # actions check 후 방향 설정
    if actions[idx][0] == time:
        if actions[idx][1] == 'D':
            d += 1
            if d >= 4: d -= 4
        else:
            d -= 1
            if d < 0: d += 4
        if idx < len(actions) - 1:
            idx += 1
        else:
            idx = 0    