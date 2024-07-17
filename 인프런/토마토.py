from collections import deque

M, N = list(map(int, input().split()))

box = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

for x in range(N):
    row = list(map(int, input().split()))

    for y in range(M):
        if row[y] == 1:
            q.append((x, y, 0))

    box.append(row)

def bfs(q):
    value = 0

    while q:
        x, y, day = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((nx, ny, day + 1))
                value = max(value, day + 1)

    return value

answer = bfs(q)
flag = False

for x in range(N):
    for y in range(M):
        if box[x][y] == 0:
            break
    else:
        break
else:
    flag = True

if flag:
    print(-1)
else:
    print(answer)