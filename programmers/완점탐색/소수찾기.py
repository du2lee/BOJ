# 소수 판별 알고리즘
def func(X):
    flag = True
    
    for v in range(2, X):
        if X % v == 0:
            flag = False
            break
    
    return flag

# 조합 구하기
def func2(s, n):
    for idx in range(len(s)):
        if n == 1:
            yield [s[idx]]
        else:
            for next in func2(s[:idx] + s[idx+1:], n - 1):
                yield [s[idx]] + next

def solution(numbers):
    d = dict()
    
    for l in range(len(numbers)):
        for V in func2(numbers, l + 1):
            # 값 붙히기
            cache = ''
            for v in V:
                cache = cache + v
                
            num = int(cache)
            
            if num >= 2:
                if func(num):
                    d[num] = func(num)
    
    return len(d)