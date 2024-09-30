def solution(number, k):
    stack = []

    for i in range(len(number)):
        num = number[i]
        
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

# 아래의 코드는 시간 초과 코드 입니다

# def func(number, k):
#     num = number[0]
#     idx = 0
#     for i in range(1, k + 1):
#         if num < number[i]:
#             idx = i
#             num = number[i]

#     return idx, num


# def solution(number, k):
#     answer = ''

#     while k > 0:
#         idx, num = func(number, k)

#         k -= idx
#         answer = answer + num
#         number = number[idx + 1:]
    
#     answer = answer + number
    
#     return answer