N = int(input())

graph= []

for i in range(N):
    graph.append(list(map(int, '1' * N)))

def func(x, y, N):
    if N == 3:
        graph[x+1][y+1] = 0
        return

    cache = N // 3
    for i in range(x, x + N, cache):
        for j in range(y, y + N, cache):
            if i == x + cache and j == y + cache:
                for idx in range(i, i+cache):
                    for idx2 in range(j, j+cache):
                        graph[idx][idx2] = 0
            else:
                func(i, j, cache)


func(0,0,N)

for x in range(N):
    for y in range(N):
        if graph[x][y] == 0:
            print(' ', end="")
        else:
            print('*' * graph[x][y], end="")
    print()

















# import sys

# def func(N):
#     global Map   

#     if N == 3:
#         Map[0][:3] = [1, 1, 1]
#         Map[2][:3] = [1, 1, 1]
#         Map[1][:3] = [1, 0, 1]
#         return 

#     a = N // 3
#     func(N // 3)
#     for i in range(3) :
#         for j in range(3) :
#             if i == 1 and j == 1 :
#                 continue
#             for k in range(a) :
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어


# N = int(sys.stdin.readline())

# Map = [[0 for i in range(N)] for i in range(N)]

# func(N)

# for i in Map :
#     for j in i :
#         if j :
#             print('*', end = '')
#         else :
#             print(' ', end = '')
#     print()