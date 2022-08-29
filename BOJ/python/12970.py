import sys

N, k = list(map(int, input().split()))

array = ['B'] * N
count = 0
flag = False

for idx in range(N):
    for i in range(N - 1, idx - 1, -1):
        if i == N - 1:
            array[i] == 'A'
        else:
            array[i + 1] = 'B'
            array[i] = 'A'
            count += 1

        if k == count:
            array[i] = 'A'
            print(''.join(array))
            flag = True
            break
    
    if flag:
        break

    count -= array.count('A')

if not(flag):
    print(-1)
    



# N ,K = map(int, sys.stdin.readline().split())

# array = ['B'] * N
# count = 0

# while array != ['A'] * N:
#     for i in range(N):
#         idx = N - 1 - i
#         if array[idx] == 'A':
#             continue
#         if idx == N -1:
#             array[idx] = 'A'
#         else:
#             array[idx + 1] = 'B'
#             array[idx] = 'A'
#             count += 1
#         if K == count:
#             print(''.join(array))
#             exit()
#     count -= 1 * array.count('A')
            
# print(-1)