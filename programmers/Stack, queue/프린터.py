from collections import deque

def solution(priorities, location):
    answer = 0
    N = len(priorities)
    stack = deque()
    
    for i in range(len(priorities)):
        stack.append((priorities[i], i))
    index = 0
        
    while stack:
        flag = False
        priority, idx = stack.popleft()
        for p, i in stack:
            if p > priority:
                stack.append((priority, idx))
                flag = True
                break
        if flag:
            continue
        
        index += 1
        if location == idx:
            answer = index
            break
        
    return answer