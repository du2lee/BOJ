N = int(input())
num = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [[0 for _ in range(N)] for _ in range(N)]

x = N // 2
y = N // 2

graph[x][y] = 1

snail = (N  - 1) // 2
cnt = 2
result = [0, 0]

for i in range(snail):
    x += dx[3]
    y += dy[3]
    graph[x][y] = cnt   # 상
    cnt += 1

    for _ in range(2 * (i + 1) - 1):    # 우
        x += dx[0]
        y += dy[0]
        graph[x][y] = cnt
        cnt += 1

    for _ in range(2 * (i + 1)):    # 하
        x += dx[2]
        y += dy[2]
        graph[x][y] = cnt
        cnt += 1

    for _ in range(2 * (i + 1)):    # 좌
        x += dx[1]
        y += dy[1]
        graph[x][y] = cnt
        cnt += 1

    for _ in range(2 * (i + 1)):    # 상
        x += dx[3]
        y += dy[3]
        graph[x][y] = cnt
        cnt += 1

for i, row in enumerate(graph):
    for j, node in enumerate(row):
        if num == node:
            result[0] = i + 1
            result[1] = j + 1
        print(node, end= ' ')
    print()

print(result[0], result[1])