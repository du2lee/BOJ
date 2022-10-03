from heapq import *

def solution(prices):
    N = len(prices)
    answer = [0] * len(prices)
    
    for i in range(N):
        for j in range(i + 1, N):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    
    return answer