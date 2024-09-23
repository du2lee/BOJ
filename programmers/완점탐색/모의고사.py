def solution(answers):
    answer = []
    
    counts = [0 ,0, 0]
    
    for idx in range(len(answers)):
        a = answers[idx]
        
        # 1번학생
        if a == idx % 5 + 1:
            counts[0] += 1
            
        # 2번학생
        arr = [2, 1, 2, 3, 2, 4, 2, 5]
        if a == arr[idx % 8]: counts[1] += 1
            
        # 3번학생
        arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
        if a == arr[idx % 10]: counts[2] += 1
        
    cache = -1

    for idx in range(3):
        if cache < counts[idx]:
            cache = counts[idx]
            answer = []
            answer.append(idx + 1)
        elif cache == counts[idx]:
            answer.append(idx + 1)
    return answer