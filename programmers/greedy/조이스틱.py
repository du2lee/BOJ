# 2024.09.30 다시 풀어봄


def solution(name):
    answer = 0

    # 스펠링 변경
    for a in name:
        num = ord(a) - 65
        answer += min(num, abs(26 - num))

    # 좌우 이동
    l = len(name)
    move = l - 1
    for i, c in enumerate(name):
        Nnode = i + 1

        while Nnode < l and name[Nnode] == 'A':
            Nnode += 1
        
        left = l - Nnode
        move = min(move, 2 * i + left, 2 * left + i)

    return answer + move



# ==============================================
# 아래는 이전에 풀었던 성공케이스 

# def solution(name):
#     answer = 0
#     N = len(name)
        
#     for i in range(N):
#         a = ord(name[i]) - 65
#         answer += min(26 - a, a)

#     minValue = N - 1
                
#     for i, c in enumerate(name):        # 핵심은 A로 이루어진 긴 문자열을 피하는 것
#         nextNode = i + 1
        
#         while nextNode < N and name[nextNode] == 'A':
#             nextNode += 1
        
#         minValue = min(minValue, 2 * i + N - nextNode, 2 * (N - nextNode) + i)
        

#     return answer + minValue














# def solution(name):
#     answer = 0
#     N = len(name)
#     graph = []
        
#     for i in range(len(name)):
#         a = ord(name[i]) - 65
#         if a != 0:
#             graph.append(i)
#             answer += min(26 - a, a)
            
#     index = 0
    
#     if graph[0] < (N - graph[-1]):
#         index = graph[0]
#         answer += index
#     else:
#         index = graph[-1]
#         answer += N - index
    
#     while len(graph) >= 2:
#         graph.remove(index)
#         minValue = N
#         index2 = 0
#         for i in graph:
#             b = abs(i - index)
#             if minValue >= min(b, N - b):
#                 minValue = min(b, N - b)
#                 index2 = i
#         answer += minValue
#         index = index2
                
        

#     return answer