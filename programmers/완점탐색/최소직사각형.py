def solution(sizes):
    X, Y = 0, 0
    
    for x, y in sizes:
        if x < y:
            x, y = y, x
        
        X, Y = max(X, x), max(Y, y)
        
    answer = X * Y
    return answer