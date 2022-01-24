import sys

# def fun(array, idx, N, K):                                                    //시간초과코드
#     if idx == N - 1:
#         count = 0
#         array[idx] = 'A'
#         for i in range(len(array)):
#             if array[i] == 'A':
#                 count += array[i+1:].count('B')
#         if count == K:
#             print(''.join(array))
#             exit()
#         count = 0
#         array[idx] = 'B'
#         for i in range(len(array)):
#             if array[i] == 'A':
#                 count += array[i+1:].count('B')
#         if count == K:
#             print(''.join(array))
#             exit()
#         return
#     array[idx] = 'A'
#     fun(array, idx + 1, N, K)
#     array[idx] = 'B'
#     fun(array, idx + 1, N, K)

# N, K = map(int, sys.stdin.readline().split())

# array = [''] * N
# fun(array, 0, N, K)
# print(-1)

N ,K = map(int, sys.stdin.readline().split())

array = ['B'] * N
count = 0

while array != ['A'] * N:
    for i in range(N):
        idx = N - 1 - i
        if array[idx] == 'A':
            continue
        if idx == N -1:
            array[idx] = 'A'
        else:
            array[idx + 1] = 'B'
            array[idx] = 'A'
            count += 1
        if K == count:
            print(''.join(array))
            exit()
    count -= 1 * array.count('A')
            
print(-1)