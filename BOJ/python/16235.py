from collections import deque

N, M, K = list(map(int, input().split()))

recharge = []
maps = [[5 for _ in range(N)] for __ in range(N)]
trees = [[deque() for _ in range(N)] for __ in range(N)]
treeLocation = deque()

dx = [1, 0, -1]
dy = [1, 0, -1]

for _ in range(N):
    recharge.append(list(map(int, input().split())))

for _ in range(M): # 이부분 최소값부터 넣는거 구현해야함
    x, y, age = list(map(int, input().split()))
    trees[x - 1][y - 1].appendleft(age)
    treeLocation.append((x - 1, y - 1))

def spring():
    life = deque()
    dead = deque()
    new = deque()

    while treeLocation:
        x, y = treeLocation.popleft()

        age = trees[x][y].popleft()
        if maps[x][y] >= age:
            maps[x][y] -= age
            life.append((x, y))
            trees[x][y].append(age + 1)
            if (age + 1) % 5 == 0:
                new.append((x, y))
        else:
            dead.append((x, y, age // 2))

    return life, dead, new

def summer(dead):
    while dead:
        x, y, feed = dead.popleft()
        maps[x][y] += feed

def fall(new):
    while new:
        x, y = new.popleft()

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                
                nx = dx[i] + x
                ny = dy[j] + y

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                trees[nx][ny].appendleft(1)
                treeLocation.appendleft((nx, ny))


for _ in range(K):
    # 봄
    treeLocation, dead, new = spring()
    # 여름
    summer(dead)
    # 가을
    fall(new)
    # 겨울
    for x in range(N):
        for y in range(N):
            maps[x][y] += recharge[x][y]

print(len(treeLocation))