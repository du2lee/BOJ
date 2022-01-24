import sys
from collections import deque

array = list([i for i in map(int,sys.stdin.readline().split())] for _ in range(9))

blank = [(x, y) for x in range(9) for y in range(9) if array[y][x] == 0]

boolean = False

def check(x, y):
    cache = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if array[i][x] in cache:
            cache.remove(array[i][x])

        if array[y][i] in cache:
            cache.remove(array[y][i])

    dx = x // 3
    dy = y // 3

    for i in range(dy * 3, (dy + 1) * 3):
        for j in range(dx * 3, (dx + 1) * 3):
            if array[i][j] in cache:
                cache.remove(array[i][j])

    return cache

def dfs(N):

    global boolean

    if boolean:
        return

    if N == len(blank):
        for y in range(9):
            for x in range(9):
                print(array[y][x], end=' ')
            print('')
    else:
        (x, y) = blank[N]
        list = check(x, y)
        for i in list:
            array[y][x] = i
            dfs(N + 1)
            array[y][x] = 0

dfs(0)

'''sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)'''