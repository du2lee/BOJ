N = int(input())

maps= [[False for _ in range(101)] for __ in range(101)]

def draw(a, b, action, d):
    actions = []

    for x, y in action:
        actions.append((x, y))

    for idx in range(len(action) - 1, -1, -1):
        x, y = action[idx]
        a -= y
        b += x
        maps[a][b] = True

        actions.append((-y, x))
    
    return a, b, actions

def func(xx, yy, d, g):
    if g == 0:
        if d == 0:
            maps[xx][yy + 1] = True
            return [xx, yy + 1, [(0, 1)]]
        elif d == 1:
            maps[xx - 1][yy] = True
            return [xx - 1, yy, [(-1, 0)]]
        elif d == 2:
            maps[xx][yy - 1] = True
            return [xx, yy - 1, [(0, -1)]]
        elif d == 3:
            maps[xx + 1][yy] = True
            return [xx + 1, yy, [(1, 0)]]
    else:
        x, y, action = func(xx, yy, d, g - 1)
        return draw(x, y, action, d)
    
for _ in range(N):
    y, x, d, g = list(map(int, input().split()))
    maps[x][y] = True
    func(x, y, d, g)

result = 0
# 사각형 구하기
for i in range(100):
    for j in range(100):
        if maps[i][j] and maps[i][j + 1] and maps[i + 1][j] and maps[i + 1][j+ 1]:
            result += 1
        
print(result)