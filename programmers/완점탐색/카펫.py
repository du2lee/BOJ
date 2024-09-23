# yellow 최대 공약수 찾기
def func(X):
    answer = []
    
    limit = X
    idx = 1
    
    while idx <= limit:
        if X % idx == 0:
            answer.append((idx, X // idx))
            limit = X // idx - 1
        
        idx += 1
        
    return answer


def solution(brown, yellow):
    answer = []
    arr = func(yellow)
    
    for x, y in arr:
        cache = x + y + 2
        
        if brown == cache * 2:
            answer = [y + 2, x + 2]
            break

    return answer