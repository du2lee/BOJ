from collections import deque
from copy import deepcopy

def func(X, Y, arr):
    counts = 0
    first, second = 1, 1
    
    q = deque()
    q.append(X)
    
    while q:
        tower = q.popleft()
        counts += 1
        cache = []
        
        for x, y in arr:
            if x == tower:
                q.append(y)
            elif y == tower:
                q.append(x)
            else:
                cache.append([x, y])
        
        arr = deepcopy(cache)
                
    return counts

def solution(n, wires):
    answer = 10e10
    
    for i in range(len(wires)):
        arr = wires[:i] + wires[i+1:]
        x, y = wires[i]
        
        countA = func(x, y, arr)
        countB = n - func(x, y, arr)
        
        answer = min(answer, abs(countA - countB))
    
    return answer