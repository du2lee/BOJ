N, M = list(map(int, input().split()))

line_w = []
line_b = []
graph = []
graph_w = []
graph_b = []

for i in range(8):
    if i % 2 == 0:
        line_w.append('W')
        line_b.append('B')
    else:
        line_b.append('W')
        line_w.append('B')

for i in range(8):
    if i % 2 == 0:
        graph_w.append(line_w)
        graph_b.append(line_b)
    else:
        graph_w.append(line_b)
        graph_b.append(line_w)

for i in range(N):
    graph.append(list(input()))

cache_x = N - 7
cache_y = M - 7

result = 64

for x in range(cache_x):
    for y in range(cache_y):
        count_w = 0
        count_b = 0
        for i in range(8):
            for j in range(8):
                if graph[i + x][j + y] != graph_w[i][j]:
                    count_w += 1
                if graph[i + x][j + y] != graph_b[i][j]:
                    count_b += 1
        if result > min(count_w, count_b):
            result = min(count_w, count_b)
print(result)
















# import sys

# x, y = map(int, sys.stdin.readline().split())

# square = []

# count_square_b = [0 for i in range(x)]
# count_square_w = [0 for i in range(x * y)]
# Min = 64

# for i in range(x):
#     value = sys.stdin.readline()
#     square.append(value)

# for k in range(x):
#     for j in range(y):
#         if (k + j) % 2 == 0:  
#             if square[k][j] != 'B':       #제일 왼쪽, 위가 블랙
#                 count_square_b[k][j] = 1
#             else:                       #제일 왼쪽, 위가 화이트
#                 count_square_w[k][j] = 1
#         else:
#             if square[k][j] != 'W':       #제일 왼쪽, 위가 블랙
#                 count_square_b[k][j] = 1
#             else:                       #제일 왼쪽, 위가 화이트
#                 count_square_w[k][j] = 1
# for i in range(x - 8):
#     sum_b = 0
#     sum_w = 0
#     for l in range(i + 8):
#         for m in range(y - 8):
#             for n in range(m + 8):
#                 sum_b += count_square_b[l][n]
#                 sum_w += count_square_w[l][n]
#     Min = min(Min,sum_b,sum_w)

# print(Min)