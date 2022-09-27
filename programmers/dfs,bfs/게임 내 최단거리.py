from heapq import *
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    INF = int(10e9)
    distance = [[0 for _ in range(M)] for _ in range(N)]
    
    q = [(0,0)]
    distance[0][0] = 1
    
    while q:
        x, y = heappop(q)
        dict = distance[x][y]
        if x == N - 1 and y == M - 1:
            return dict
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue
            if maps[nx][ny] == 1 and (distance[nx][ny] == 0 or distance[nx][ny] > dict + 1):
                distance[nx][ny] = dict + 1
                heappush(q,(nx, ny))
    
    return -1