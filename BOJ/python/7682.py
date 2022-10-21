def checkFunction(graph, player):
    for i in range(0, 3):
        if graph[i][0] == graph[i][1] == graph[i][2] == player:
            return True
        if graph[0][i] == graph[1][i] == graph[2][i] == player:
            return True

    if graph[0][0] == graph[1][1] == graph[2][2] == player:
        return True
    if graph[2][0] == graph[1][1] == graph[0][2] == player:
        return True
    return False

while True:
    board = input()
    if board == 'end':
        break

    countX = board.count('X')
    countO = board.count('O')
    countDot = board.count('.')

    countX_O = countX - countO

    if countX_O >= 2 or countX_O < 0:
        print('invalid')
        continue

    graph = []
    for i in range(0, 9, 3):
        graph.append(board[i:i+3])

    if checkFunction(graph, 'X') and not(checkFunction(graph, 'O')) and countX_O == 1:
        print('valid')
        continue

    if checkFunction(graph, 'O') and not(checkFunction(graph, 'X')) and countX_O == 0:
        print('valid')
        continue
    
    if countX == 5 and countO == 4 and not(checkFunction(graph, 'O')):
        print('valid')
        continue 
    
    print('invalid')