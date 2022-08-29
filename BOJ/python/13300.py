N, K = list(map(int, input().split()))

rooms = [[0,0,0,0,0,0], [0,0,0,0,0,0]]

# count members
for i in range(N):
    a, b = list(map(int, input().split()))
    rooms[a][b-1] += 1

# count rooms
for i in range(2):
    for j in range(6):
        if rooms[i][j] % K == 0:
            rooms[i][j] = rooms[i][j] // K
        else:
            rooms[i][j] = (rooms[i][j] // K) + 1

print(sum(rooms[0]) + sum(rooms[1]))