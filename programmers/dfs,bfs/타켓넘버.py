def solution(numbers, target):
    
    def dfs(idx, count, answer):
        if idx == len(numbers):
            if count == target:
                answer += 1
            return answer
        
        count += numbers[idx]
        answer = dfs(idx + 1, count, answer)
        
        count -= numbers[idx]
        count -= numbers[idx]
        
        answer = dfs(idx + 1, count, answer)

        return answer
        
    return dfs(0, 0, 0)

print(solution([4, 1, 2, 1], 2))
        