def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        cache = array[i-1:j]
        cache.sort()
        answer.append(cache[k-1])
    
    return answer