N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

for x in range(N):
    for y in range(N):
        count = 0
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if N <= nx or nx < 0 or N <= ny or ny < 0:
                count += 1
                continue
                
            if graph[x][y] > graph[nx][ny]:
                count += 1
        
        if count == 4:
            answer += 1

print(answer)
            