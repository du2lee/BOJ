# 2024.09.30

def solution(n, lost, reserve):
    answer = 0
    check = [1] * (n + 1)
    dx = [-1, 1]
    
    for num in lost:
        check[num] -= 1
    
    for num in reserve:
        check[num] += 1

    for num in range(1, n + 1):
        if check[num] == 2:
            for i in dx:
                nx = num + i
                if nx < 1 or nx > n:
                    continue

                if check[nx] == 0:
                    check[nx] += 1
                    check[num] -= 1
                    break
                
    for v in check[1:]:
        if v > 0:
            answer += 1
    
    return answer

# def solution(n, lost, reserve):
#     answer = 0
#     check = [1] * (n + 1)
#     dx = [-1, 1]
    
#     for num in lost:
#         check[num] = 0
    
#     for num in reserve:
#         for a in dx:
#             nx = num + a
#             if nx < 1 or nx > n:
#                 continue
            
#             if check[nx] == 0:
#                 check[nx] = 1
#                 break 
                
#     for v in check[1:]:
#         if v > 0:
#             answer += 1

#     return answer



# 아래는 옛날에 풀었던 성공케이스 입니다.

# def solution(n, lost, reserve):
#     answer = n
#     lost.sort()
#     reserve.sort()
    
#     check_lost = [True] * len(lost)
#     check_reserve = [True] * len(reserve)
    
#     # 잃어버렸는데 여유분 있는 경우 
#     for i in range(len(lost)):
#         for j in range(len(reserve)):
#             if lost[i] == reserve[j]:
#                 check_lost[i] = False
#                 check_reserve[j] = False
    
#     # 빌려주기
    
#     for i in range(len(lost)):
#         if not(check_lost[i]):
#             continue
#         for j in range(len(reserve)):
#             if check_reserve[j] and (lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]):
#                 check_reserve[j] = False
#                 check_lost[i] = False
#                 break
                
#     for i in check_lost:
#         if i:
#             answer -= 1
    
#     return answer