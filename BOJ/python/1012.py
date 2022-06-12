import sys


def dfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
value_list = list()

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    maps = [[0] * N for _ in range(M)]
    graph = dict()


    for node in range(1, M * N + 1):                                # graph 초기화
        graph[node] = []
    
    
    for _ in range(K):                                              #   좌표 input
        x, y = map(int, sys.stdin.readline().split())
        maps[x][y] = 1
    
    
    for node in range(1, M * N + 1):                                #   maps를 이용해서 graph 만들기
        node_x = int((node - 1) / N)
        node_y = (node - 1) % N
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if (nx < 0 or ny < 0  or nx >= M or ny >= N):
                continue
            if maps[node_x][node_y] != 0 and maps[nx][ny] != 0:
                graph[node].append(nx * N + ny + 1)
 
 
        if maps[node_x][node_y] != 0 and graph[node] == []:         #   자신혼자만 값을 가질경우(주위에 전부 값이 없을 경우)
            count += 1
  
  
    for node in range(1, M * N + 1):                                #   dfs를 이용해서 연결되어있는 값들 count
        cache = dfs(graph, node)
        if cache != [node]:
            cache.sort()
            if cache not in value_list:
                value_list.append(cache)
    count += len(value_list)
    print(count)
        

            