import sys
from collections import deque                                              # 시간복잡도 때매 deque씀

M, N = map(int, sys.stdin.readline().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

maps = list()
queue = deque()
distance = [0 for _ in range(M * N)]
count_1 = 0
count__1 = 0
count_0 = 0
count = 0

for _ in range(N):
    cache = [i for i in map(int, sys.stdin.readline().split())]             # map 그리기
    maps.append(cache)

for node in range(M * N):                                                   # 시작 위치 설정 and count value of 1, -1
    if maps[int(node / M)][node % M] == 1:
        queue.append(node)
        distance[node] = 1
        count_1 += 1
    elif maps[int(node / M)][node % M] == -1:
        count__1 +=1
    else:
        count_0 += 1

if count__1 + count_1 == M * N:                                             # 모든 토마토가 다 익었음
    print(0)
else:
    while queue:
        node = queue.popleft()
        node_y = int(node / M)
        node_x = node % M
        if maps[node_y][node_x] == 1:
            for i in range(4):
                ny = dy[i] + node_y
                nx = dx[i] + node_x
                if ny < 0 or nx < 0 or ny >= N or nx >= M:
                    continue
                if distance[ny * M + nx] == 0 and maps[ny][nx] == 0:
                    distance[ny * M + nx] = distance[node] + 1
                    queue.append(ny * M + nx)
                    maps[ny][nx] = 1
                    count += 1
    if count == count_0:
        print(max(distance) - 1)
    else:
        print(-1)