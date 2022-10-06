def solution(citations):
    answer = 0
    citations.sort()
    N = len(citations)
    flag = False
    array = [0]
    
    
    for i in range(citations[-1]):
        for j in range(N):
            if citations[j] >= i:
                if N - j >= i and j <= i:
                    array.append(i)
                else:
                    flag = True
                break
        if flag:
            break
            
    answer = array[-1]
    
    
    return answer