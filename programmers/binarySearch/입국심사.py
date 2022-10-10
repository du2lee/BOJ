def solution(n, times):
    answer = 0
    times.sort()
    
    left, right = 1, n * times[-1]
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for i in times:
            people += mid // i
            
            if people >= n:
                break 
        if people < n:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer