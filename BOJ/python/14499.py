dice = [0, 0, 0, 0, 0, 0]
maps = []

def check(x, y, direction, N, M):
    if direction == 1:
        y += 1
        if y >= M:
            return False
    elif direction == 2:
        y -= 1
        if y < 0:
            return False
    elif direction == 3:
        x -= 1
        if x < 0:
            return False
    elif direction == 4:
        x += 1
        if x >= N:
            return False
    return True

def turn(dice, direction):
    if direction == 1:
        return [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif direction == 2:
        return [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif direction == 3:
        return [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif direction == 4:
        return [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    
def location(x, y, direction):
    if direction == 1:
        return (x, y + 1)
    elif direction == 2:
        return (x, y - 1)
    elif direction == 3:
        return (x - 1, y)
    elif direction == 4:
        return (x + 1, y)
    
N, M, x, y, K = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(N)]

command = list(map(int, input().split()))

for i in command:
    if check(x, y, i, N, M):
        dice = turn(dice, i)
        x, y = location(x, y, i)

        if maps[x][y] == 0:
            maps[x][y] = dice[0]
        else:
            dice[0] = maps[x][y]
            maps[x][y] = 0
        print(dice[5])