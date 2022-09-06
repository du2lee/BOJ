from collections import deque


N, M = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    count = 1
    result = 0

    while queue:
        length = len(queue)
        for _ in range(length):
            v = queue.popleft()
            if v[0] == N - 1 and v[1] == M - 1:
                result = count

            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if nx < 0 or N <= nx or ny < 0 or M <= ny:
                    continue
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0
        count += 1
    return result

for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0, 0))









# import sys

# N, M = map(int, sys.stdin.readline().split())
# maps = list()
# distance = [0 for _ in range(N * M)]
# q = list()
# graph = dict()

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for node in range(1, N * M + 1):
#     graph[node] = []

# for _ in range(N):
#     row = input()
#     maps.append(row)

# q.append(0)
# distance[0] = 1

# while q:
#     node = q.pop(0)
#     if distance[node] != 0:
#         node_x = int(node / M)
#         node_y = node % M
#         for i in range(4):
#             nx = node_x + dx[i]
#             ny = node_y + dy[i]
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#             if maps[node_x][node_y] == '1' and maps[nx][ny] == '1' and distance[nx * M + ny] == 0:
#                 distance[nx * M + ny] = distance[node_x * M + node_y] + 1
#                 q.append(nx * M + ny)
#     if node == M * N - 1:
#         print(distance[M * N - 1])
#         break