dx = [1, -1, 0]
dy = [0, 1, -1]

def dfs(x, y, w, h):
    global count
    graph[x][y] = 0

    for i in range(3):
        for j in range(3):
            x1 = dx[i] + x
            y1 = dy[j] + y
            if x1 < 0 or h <= x1 or y1 < 0 or w <= y1:
                continue
            if graph[x1][y1] == 1:
                dfs(x1, y1, w, h)

while True:
    w, h = list(map(int, input().split()))

    if w == 0 and h == 0:
        break

    graph = []
    count = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y, w, h)
                count += 1

    print(count)