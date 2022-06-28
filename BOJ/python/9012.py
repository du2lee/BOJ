# import sys
# from collections import deque

# N = int(sys.stdin.readline())

# for _ in range(N):
#     value = input()
#     stack = deque(value)
#     count_r = 0
#     count_l = 0
#     while stack:
#         poped = stack.pop()
#         if poped == ')':
#             count_r += 1
#         elif poped == '(':
#             count_l += 1
#         if count_r - count_l < 0:
#             break
        
#     if count_r == count_l:
#         print('YES')
#     else:
#         print('NO')        


N = int(input())

for _ in range(N):
    array = input()
    open = 0
    close = 0

    for idx in array:
        if idx == '(':
            open += 1
        elif idx == ')':
            close += 1
        if open < close:
            break

    if close == open:
        print('YES')
    else:
        print('NO')