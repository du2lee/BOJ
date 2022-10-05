def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    
    check_lost = [True] * len(lost)
    check_reserve = [True] * len(reserve)
    
    # 잃어버렸는데 여유분 있는 경우 
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                check_lost[i] = False
                check_reserve[j] = False
    
    # 빌려주기
    
    for i in range(len(lost)):
        if not(check_lost[i]):
            continue
        for j in range(len(reserve)):
            if check_reserve[j] and (lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]):
                check_reserve[j] = False
                check_lost[i] = False
                break
                
    for i in check_lost:
        if i:
            answer -= 1
    
    return answer