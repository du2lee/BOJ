from copy import deepcopy

# 모든 경우의 수
def func(arr, n):
    for idx in range(len(arr)):
        if n == 1:
            yield [arr[idx]]
        else:
            for next in func(arr[:idx] + arr[idx + 1 :], n - 1):
                yield [arr[idx]] + next

def solution(k, dungeons):
    answer = -1
    
    cache = deepcopy(k)
    
    for root in func(dungeons, len(dungeons)):
        k = deepcopy(cache)
        counts = 0
        for x, y in root:
            if k >= x:
                counts += 1
                k -= y
        answer = max(answer, counts)
        
    return answer