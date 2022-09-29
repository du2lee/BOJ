def solution(s):
    answer = True
    count = 0
    
    for idx in s:
        if idx == '(':
            count += 1
        elif idx == ')':
            count -= 1
        if count < 0:
            answer = False
            break
            
    if count != 0:
        answer = False

    return answer