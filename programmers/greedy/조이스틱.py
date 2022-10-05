def solution(name):
    answer = 0
    N = len(name)
        
    for i in range(N):
        a = ord(name[i]) - 65
        answer += min(26 - a, a)
    minValue = N - 1
                
    for i, c in enumerate(name):        # 핵심은 A로 이루어진 긴 문자열을 피하는 것
        nextNode = i + 1
        
        while nextNode < N and name[nextNode] == 'A':
            nextNode += 1
        
        minValue = min(minValue, 2 * i + N - nextNode, 2 * (N - nextNode) + i)
        

    return answer + minValue














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