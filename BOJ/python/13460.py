from copy import deepcopy

def up(graphs, x, y, flag):
    xx, yy = x, y
    for i in range(x - 1, 0, -1):
        if graphs[i][y] == 'O':
            xx, yy = -2, -2
            break
        if graphs[i][y] == '#' or graphs[i][y] == 'R' or graphs[i][y] == 'B':
            break
        xx = i
    graphs[x][y] = '.'
    if not(xx == -2 and yy == -2):
        if flag:
            graphs[xx][yy] = 'R'
        else:
            graphs[xx][yy] = 'B'
    return graphs, xx, yy

def down(graphs, x, y, flag):
    xx, yy = x, y
    for i in range(x + 1, N):
        if graphs[i][y] == 'O':
            xx, yy = -2, -2
            break
        if graphs[i][y] == '#' or graphs[i][y] == 'R' or graphs[i][y] == 'B':
            break
        xx = i
    graphs[x][y] = '.'
    if not(xx == -2 and yy == -2):
        if flag:
            graphs[xx][yy] = 'R'
        else:
            graphs[xx][yy] = 'B'
    return graphs, xx, yy

def left(graphs, x, y, flag):
    xx, yy = x, y
    for i in range(y - 1, 0, -1):
        if graphs[x][i] == 'O':
            xx, yy = -2, -2
            break
        if graphs[x][i] == '#' or graphs[x][i] == 'R' or graphs[x][i] == 'B':
            break
        yy = i
    graphs[x][y] = '.'
    if not(xx == -2 and yy == -2):
        if flag:
            graphs[xx][yy] = 'R'
        else:
            graphs[xx][yy] = 'B'
    return graphs, xx, yy

def right(graphs, x, y, flag):
    xx, yy = x, y
    for i in range(y + 1, M):
        if graphs[x][i] == 'O':
            xx, yy = -2, -2
            break
        if graphs[x][i] == '#' or graphs[x][i] == 'R' or graphs[x][i] == 'B':
            break
        yy = i
    graphs[x][y] = '.'
    if not(xx == -2 and yy == -2):
        if flag:
            graphs[xx][yy] = 'R'
        else:
            graphs[xx][yy] = 'B'
    return graphs, xx, yy

def move(graphs, rx, ry, bx, by, d):
    Rx, Ry, Bx, By = rx, ry, bx, by
    cache = graphs
    if d == 1:
        if ry == by and rx > bx:
                cache, Bx, By = up(graphs, bx, by, False)
                cache, Rx, Ry = up(graphs, rx, ry, True)
        else:
            cache, Rx, Ry = up(graphs, rx, ry, True)
            cache, Bx, By = up(graphs, bx, by, False)
            
    elif d == 2:
        if ry == by and rx < bx:
                cache, Bx, By = down(graphs, bx, by, False)
                cache, Rx, Ry = down(graphs, rx, ry, True)
        else:
            cache, Rx, Ry = down(graphs, rx, ry, True)
            cache, Bx, By = down(graphs, bx, by, False)
    elif d == 3:
        if rx == bx and ry > by:
                cache, Bx, By = left(graphs, bx, by, False)
                cache, Rx, Ry = left(graphs, rx, ry, True)
        else:
            cache, Rx, Ry = left(graphs, rx, ry, True)
            cache, Bx, By = left(graphs, bx, by, False)
    elif d == 4:
        if rx == bx and ry < by:
                cache, Bx, By = right(graphs, bx, by, False)
                cache, Rx, Ry = right(graphs, rx, ry, True)
        else:
            cache, Rx, Ry = right(graphs, rx, ry, True)
            cache, Bx, By = right(graphs, bx, by, False)

    return cache, Rx, Ry, Bx, By

answer = -1

def dfs(graphs, rx, ry, bx, by, count, d):
    global answer
    if count > 10:
        return
    else:
        temp = deepcopy(graphs)
        for i in range(1, 5):
            if d == i:
                continue
            graphs = deepcopy(temp)
            cache, Rx, Ry, Bx, By = move(graphs, rx, ry, bx, by, i)
            if Bx == -2 and By == -2:
                continue
            elif Rx == -2 and Ry == -2:
                if answer == -1 or answer > count:
                    answer = count
                continue
            elif rx == Rx and ry == Ry and bx == By and by == By:
                pass
            else:
                dfs(cache, Rx, Ry, Bx, By, count + 1, i)


N, M = list(map(int, input().split()))
maps = [list(input()) for _ in range(N)]

rx, ry, bx, by = -1, -1, -1, -1

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'R':
            rx, ry = i, j
        elif maps[i][j] == 'B':
            bx, by = i, j

dfs(maps, rx, ry, bx, by, 1, 0)
print(answer)