def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    countWorks = 0
    idx = 0
    while countWorks < N:
        cache = 0
        
        for i in range(idx, N):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 and i <= idx:
                cache += 1
                idx += 1
  
        if cache != 0:
            answer.append(cache)
            countWorks += cache
    
    return answer