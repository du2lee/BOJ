def solution(clothes):
    answer = 1
    closet = dict()
    
    for tool, type in clothes:
        closet[type] = []
    
    for tool, type in clothes:
        closet[type].append(tool)
        
    
    for type in closet:
        answer *= (len(closet[type]) + 1)
    
    return answer - 1