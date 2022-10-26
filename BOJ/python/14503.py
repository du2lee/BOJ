N, M = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

answer = 0

while True:
    # 방문
    if graph[x][y] == 0:
        graph[x][y] = 2
        answer += 1
    flag = True

    # 왼쪽부터 확인
    for i in range(1, 5):
        j = d - i
        if j < 0: j += 4
        nx = x + dx[j]
        ny = y + dy[j]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 0:
            x, y, d = nx, ny, j
            flag = False
            break

    # 뒤로 이동
    if flag:
        nx = x + dx[d - 2]
        ny = y + dy[d - 2]
        
        if graph[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
 
print(answer)