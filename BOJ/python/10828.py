# import sys
# from collections import deque

# def push(stack, value):
#     stack.append(value)
# def pop(stack):
#     if size(stack) <= 0:
#         return -1
#     return stack.pop()
# def size(stack):
#     return len(stack)
# def empty(stack):
#     if size(stack) <= 0:
#         return 1
#     return 0
# def top(stack): 
#     if size(stack) <= 0:
#         return -1
#     return stack[-1]


# stack = deque()
# N = int(sys.stdin.readline())

# for _ in range(N):
#     cache = input().split()
#     if cache[0] == 'push':
#         push(stack,int(cache[1]))
#     elif cache[0] == 'pop':
#         value = pop(stack)
#         print(value)
#     elif cache[0] == 'size':
#         value = size(stack)
#         print(value)
#     elif cache[0] == 'empty':
#         value = empty(stack)
#         print(value)
#     elif cache[0] == 'top':
#         value = top(stack)
#         print(value)
