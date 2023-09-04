from copy import deepcopy

N, M = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(N)]
cctv = []
mode = [[],
        [[0],[1],[2],[3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2],[0, 1, 3],[0, 2, 3],[1, 2, 3]],
        [[0, 1, 2, 3]],
        ]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x in range(N):
    for y in range(M):
        if maps[x][y] == 0 or maps[x][y] == 6:
            continue
        cctv.append((maps[x][y], x, y))

def draw(maps, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if maps[nx][ny] == 6:
                break
            elif maps[nx][ny] == 0:
                maps[nx][ny] = '#'


def dfs(depth, array):
    global result

    if depth == len(cctv):
        count = 0
        for i in range(N):
            for j in range(M):
                if array[i][j] == 0:
                    count += 1
        result = min(result, count)
        return
    
    temp = deepcopy(array)
    value, x, y = cctv[depth]
    for idx in mode[value]:
        draw(temp, idx, x, y)
        dfs(depth + 1, temp)
        temp = deepcopy(array)

result = int(1e9)
dfs(0, maps)
print(result)

















# 틀렸습니다 코드

# def checkNorth(x, y, mode):
#     count = 0
#     for idx in range(x - 1, -1, -1):
#         if maps[idx][y] == 6:
#             break
#         elif maps[idx][y] == 0:
#             count += 1
#             if mode:
#                 maps[idx][y] = '#'
#     return count

# def checkSouth(x, y, mode):
#     count = 0
#     for idx in range(x + 1, N):
#         if maps[idx][y] == 6:
#             break
#         elif maps[idx][y] == 0:
#             count += 1
#             if mode:
#                 maps[idx][y] = '#'
#     return count

# def checkWest(x, y, mode):
#     count = 0
#     for idx in range(y - 1, -1, -1):
#         if maps[x][idx] == 6:
#             break
#         elif maps[x][idx] == 0:
#             count += 1
#             if mode:
#                 maps[x][idx] = '#'
#     return count

# def checkEast(x, y, mode):
#     count = 0
#     for idx in range(y + 1, M):
#         if maps[x][idx] == 6:
#             break
#         elif maps[x][idx] == 0:
#             count += 1
#             if mode:
#                 maps[x][idx] = '#'
#     return count

# # check 5
# for x, y in check[5]:
#     checkEast(x, y, True)
#     checkWest(x, y, True)
#     checkNorth(x, y, True)
#     checkSouth(x, y, True)
    
# # check 4
# for x, y in check[4]:
#     east = checkEast(x, y, False)
#     west = checkWest(x, y, False)
#     north = checkNorth(x, y, False)
#     south = checkSouth(x, y, False)
#     minValue = min(min(east, west), min(north, south))
#     if minValue == east:
#         checkWest(x, y, True)
#         checkNorth(x, y, True)
#         checkSouth(x, y, True)
#     elif minValue == west:
#         checkEast(x, y, True)
#         checkNorth(x, y, True)
#         checkSouth(x, y, True)
#     elif minValue == south:
#         checkWest(x, y, True)
#         checkNorth(x, y, True)
#         checkEast(x, y, True)
#     elif minValue == north:
#         checkWest(x, y, True)
#         checkEast(x, y, True)
#         checkSouth(x, y, True)

# # check 3
# for x, y in check[3]:
#     east = checkEast(x, y, False)
#     west = checkWest(x, y, False)
#     north = checkNorth(x, y, False)
#     south = checkSouth(x, y, False)
#     maxValue = max(east + north, west + north, east + south, west + south)
#     if maxValue == west + north:
#         checkWest(x, y, True)
#         checkNorth(x, y, True)
#     elif maxValue == east + south:
#         checkEast(x, y, True)
#         checkSouth(x, y, True)
#     elif maxValue == east + north:
#         checkNorth(x, y, True)
#         checkEast(x, y, True)
#     elif maxValue == west + south:
#         checkWest(x, y, True)
#         checkSouth(x, y, True)

# # check 2
# for x, y in check[2]:
#     width = checkEast(x, y, False) + checkWest(x, y, False)
#     height = checkNorth(x, y, False) + checkSouth(x, y, False)
#     if width < height:
#         checkNorth(x, y, True)
#         checkSouth(x, y, True)
#     else:
#         checkEast(x, y, True)
#         checkWest(x, y, True)

# # check 1
# for x, y in check[1]:
#     east = checkEast(x, y, False)
#     west = checkWest(x, y, False)
#     north = checkNorth(x, y, False)
#     south = checkSouth(x, y, False)
#     maxValue = max(max(east, west), max(north, south))
#     if maxValue == east:
#         checkEast(x, y, True)
#     elif maxValue == west:
#         checkWest(x, y, True)
#     elif maxValue == south:
#         checkSouth(x, y, True)
#     elif maxValue == north:
#         checkNorth(x, y, True)

# result = 0
# for i in range(N):
#     for j in range(M):
#         if maps[i][j] == 0:
#             result += 1
# print(result)