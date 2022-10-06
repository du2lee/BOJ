def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
        
    numbers.sort(key = lambda x : x * 4, reverse = True)
    for i in numbers:
        answer += i
    
    answer = str(int(answer))
    
    return answer