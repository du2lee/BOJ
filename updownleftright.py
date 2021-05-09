import sys

N = int(sys.stdin.readline())

x, y = 0 , 0

list_move = sys.stdin.readline().split()
move_type = ['U', 'D', 'L', 'R']
move_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(len(list_move)):
    for j in range(len(move_type)): #if문 단축
        if (list_move[i] == move_type[j]):
            if (j == 0 and y <= 0) or (j == 2 and x <= 0) or (j == 3 and x >= N) or (j == 1 and y >= N):
                pass
            else:
                x += move_direction[j][0]
                y += move_direction[j][1]

print(x, y)