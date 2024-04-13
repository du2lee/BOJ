from collections import deque
from copy import deepcopy

N = int(input())

graph = []

for i in range(N):
    graph.append(deque(map(int, input().split())))

def left(maps):
    for i in range(N):
        cursor = 0
        for j in range(N):  
            value = maps[i][j]
            if value != 0:
                maps[i][j] = 0

                if maps[i][cursor] == 0:
                    maps[i][cursor] = value
                elif maps[i][cursor] == value:
                    maps[i][cursor] *= 2
                    cursor += 1
                    continue
                else:
                    cursor += 1
                    maps[i][cursor] = value              
    return maps


def right(maps):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):
            value = maps[i][j]
            if value != 0:
                maps[i][j] = 0

                if maps[i][cursor] == 0:
                    maps[i][cursor] = value
                elif maps[i][cursor] == value:
                    maps[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    maps[i][cursor] = value
                    
    return maps


def up(maps):
    for j in range(N):
        cursor = 0
        for i in range(N):  
            value = maps[i][j]
            if value != 0:
                maps[i][j] = 0

                if maps[cursor][j] == 0:
                    maps[cursor][j] = value
                elif maps[cursor][j] == value:
                    maps[cursor][j] *= 2
                    cursor += 1
                    continue
                else:
                    cursor += 1
                    maps[cursor][j] = value              
    return maps


def down(maps):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):  
            value = maps[i][j]
            if value != 0:
                maps[i][j] = 0

                if maps[cursor][j] == 0:
                    maps[cursor][j] = value
                elif maps[cursor][j] == value:
                    maps[cursor][j] *= 2
                    cursor -= 1
                    continue
                else:
                    cursor -= 1
                    maps[cursor][j] = value              
    return maps

answer = 2

def func(count, maps):
    global answer
    if count >= 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, maps[i][j])
        return

    for i in range(4):
        cache = deepcopy(maps) 
        if i == 0:
            func(count + 1, left(cache))
        elif i == 1:
            func(count + 1, right(cache))
        elif i == 2:
            func(count + 1, up(cache))
        else:
            func(count + 1, down(cache))

func(0, graph)
print(answer)





# def process(line, now): # 게임처럼 구현 -> 문제는 더 간단함을 원함
#     while line:
#         last = line.pop()

#         if last == now:
#             now *= 2
#         else:
#             line.append(last)
#             line.append(now)
#             break
        
#         if len(line) == 0:
#             line.append(now)
#             break

#     return line

# def up(maps):
#     column = [deque() for _ in range(N)]

#     # process
#     for j in range(N):
#         for i in range(N):
#             value = maps[i][j]
#             if value != 0:
#                 if len(column[j]) > 0:
#                     column[j] = process(column[j], value)
#                     continue
#                 column[j].append(value)

#     # draw
#     for j in range(N):
#         l = len(column[j])
#         for i in range(l):
#             maps[i][j] = column[j][i]
#         for i in range(l, N):
#             maps[i][j] = 0

#     return maps

# def down(maps):
#     column = [deque() for _ in range(N)]

#     # process
#     for j in range(N):
#         for i in range(N - 1, -1, -1):
#             value = maps[i][j]
#             if value != 0:
#                 if len(column[j]) > 0:
#                     column[j] = process(column[j], value)
#                     continue
#                 column[j].append(value)

#     # draw
#     for j in range(N):
#         l = len(column[j])
#         for i in range(l):
#             maps[N - 1 - i][j] = column[j][i]
#         for i in range(l, N):
#             maps[N - 1 - i][j] = 0
#     return maps

# def left(maps):
#     row = [deque() for _ in range(N)]

#     # process
#     for i in range(N):
#         for j in range(N):
#             value = maps[i][j]
#             if value != 0:
#                 if len(row[i]) > 0:
#                     row[i] = process(row[i], value)
#                     continue
#                 row[i].append(value)

#     # draw
#     for i in range(N):
#         l = len(row[i])
#         for j in range(l):
#             maps[i][j] = row[i][j]
#         for j in range(l, N):
#             maps[i][j] = 0
#     return maps

# def right(maps):
#     row = [deque() for _ in range(N)]

#     # process
#     for i in range(N):
#         for j in range(N - 1, -1, -1):
#             value = maps[i][j]
#             if value != 0:
#                 if len(row[i]) > 0:
#                     row[i] = process(row[i], value)
#                     continue
#                 row[i].append(value)

#     # draw
#     for i in range(N):
#         l = len(row[i])
#         for j in range(l):
#             maps[i][N - 1 - j] = row[i][j]
#         for j in range(l, N):
#             maps[i][N - 1 - j] = 0
#     return maps



# answer = 2

# def func(count, maps):
#     global answer
#     if count >= 5:
#         for i in range(N):
#             for j in range(N):
#                 answer = max(answer, maps[i][j])
#         return

#     for i in range(4):
#         cache = deepcopy(maps) 
#         if i == 0:
#             func(count + 1, left(cache))
#         elif i == 1:
#             func(count + 1, right(cache))
#         elif i == 2:
#             func(count + 1, up(cache))
#         else:
#             func(count + 1, down(cache))

# func(0, graph)
# print(answer)