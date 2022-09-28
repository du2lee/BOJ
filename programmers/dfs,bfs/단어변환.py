def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    def dfs(v, num, result, answer):
        if v == target and answer > num:
            answer = num
            return answer
        
        for word in words:
            if word in result:
                continue
            cache = 0
            for idx in range(len(begin)):
                if v[idx] != word[idx]:
                    cache += 1
                    
            if cache == 1:  
                result.add(word)
                answer = dfs(word, num + 1, result, answer)
                result.remove(word)
        return answer
                    
        
    answer = dfs(begin, 0, set(), int(10e9))

        
    return answer