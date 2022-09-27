N, M = list(map(int, input().split()))
INF = int(10e9)
graph = []
result = [INF] * (N + 1)

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    graph.append((a, b, c))

def func(start):
    result[start] = 0

    for _ in range(N): # _ = N -1 일때는 체크 용도
        for node, neighbor, dict in graph:
            if result[node] != INF and result[neighbor] > result[node] + dict:
                result[neighbor]  = result[node] + dict
                if _ == N - 1:
                    return True
    
    return False

flag = func(1)

if flag:
    print(-1)
else:
    for i in range(2, N + 1):
        if result[i] == INF:
            print(-1)
        else:
            print(result[i])


# N , M = list(map(int, input().split()))
# INF = 10e9

# graph = [[]for _ in range(N + 1)]
# result = [INF] * (N + 1)

# for _ in range(M):
#     A, B, C = list(map(int, input().split()))
#     graph[A].append([B, C])


# def func(start):
#     pre = [-1] * (N + 1)

#     result[start] = 0

#     for _ in range(1, N):                                   # v - 1까지 반복
#         for node in range(1, N + 1):    
#             for neighbor, dict in graph[node]:
#                 if result[neighbor] > result[node] + dict:
#                     result[neighbor] = result[node] + dict
#                     pre[neighbor] = node

#     for node in range(1, N + 1):
#         for neighbor, dict in graph[node]:
#             if result[neighbor] > dict + result[node]:
#                 return -1

#     return pre

# a = func(1)

# if a == -1:
#     print(a)
# else:  
#     for i in result[2:]:
#         if i == INF:
#             print(-1)
#         else:
#             print(i)