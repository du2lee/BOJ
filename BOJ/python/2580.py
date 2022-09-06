sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append([i, j])

def checkLow(x, value):
    for i in range(9):
        if sudoku[x][i] == value:
            return False
    return True

def checkColumn(y, value):
    for i in range(9):
        if sudoku[i][y] == value:
            return False
    return True

def checkSquare(x, y, value):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if sudoku[i][j] == value:
                return False
    return True


def dfs(v):
    if v == len(zeros):
        for i in sudoku:
            for j in i:
                print(j, end = ' ')
            print()
        exit(0)
    for i in range(1, 10):
        if checkLow(zeros[v][0], i) and checkColumn(zeros[v][1], i) and checkSquare(zeros[v][0], zeros[v][1], i):
            sudoku[zeros[v][0]][zeros[v][1]] = i
            dfs(v + 1)
            sudoku[zeros[v][0]][zeros[v][1]] = 0

dfs(0)