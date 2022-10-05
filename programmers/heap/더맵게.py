from heapq import *

def solution(scoville, K):
    answer = 0
    flag = True
    heapify(scoville)
    while len(scoville) > 1:
        answer += 1
        f = heappop(scoville)
        s = heappop(scoville)
        heappush(scoville, f + 2 * s)
        if scoville[0] >= K:
            flag = False
            break  
    if flag:
        answer = -1
    
    return answer