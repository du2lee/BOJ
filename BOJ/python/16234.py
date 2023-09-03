from collections import deque
import sys

input = sys.stdin.readline

N, L, R = list(map(int, input().split()))
nations = [list(map(int, input().split())) for _ in range(N)]

days = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    array = []

    while(q):
        x, y = q.popleft()
        check[x][y] = True
        array.append((x, y))

        for idx in range(4):
            nx = dx[idx] + x
            ny = dy[idx] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if check[nx][ny]:
                continue

            if abs(nations[nx][ny] - nations[x][y]) >= L and abs(nations[nx][ny] - nations[x][y]) <= R:
                q.append((nx, ny))

    return array


while(True):
    flag = True
    # 국경 폐쇄 초기화
    check = [[False] * N for _ in range(N)]
    for X in range(N):
        for Y in range(N):
            # 국경 개방
            array = bfs(X, Y)

            # 국경 개방 국가 없음 처리
            if len(array) > 1:
                # 인구 이동 체크
                flag = False

                # 인구 이동 전 카운트
                people = 0
                for nx, ny in array:
                    people += nations[nx][ny]

                # 인구 이동
                for nx, ny in array:
                    nations[nx][ny] = people // len(array)

    if flag:
        break

    # 날짜 카운트
    days += 1

print(days)




##################


from collections import deque

n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union               

result = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                
                if len(country) > 1:
                    flag = 1
                    people = sum(A[x][y] for x, y in country) // len(country)
                    
                    for x, y in country:
                        A[x][y] = people
    
    if flag == 0:
        print(result)
        break

    result += 1