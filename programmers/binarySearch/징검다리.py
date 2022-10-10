def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 1, distance
    
    while start <= end:
        mid = (start + end) // 2
        idx = 0
        count = 0
        
        for rock in rocks:
            if rock - idx >= mid:
                idx = rock
                continue
            count += 1
            
            if count > n:
                break
                
        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer