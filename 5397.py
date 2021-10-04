import sys
from collections import deque

T = int(sys.stdin.readline())

# for _ in range(T):                                                            //시간초과
#     strInput = input()
#     location = 0
#     stack = list()
#     for i in range(len(strInput)):
#         if strInput[i] == '<':
#             if location < 1:
#                 location = 0
#             else:
#                 location -= 1
#         elif strInput[i] == '>':
#             if location > len(stack) - 1:
#                 location = len(stack) - 1
#             else:
#                 location += 1
#         elif strInput[i] == '-':
#             if len(stack) != 0:
#                 if location == 0:
#                     continue
#                 location -= 1
#                 stack.pop(location)
#         else:
#             stack.insert(location, strInput[i])
#             location += 1
#     print(''.join(stack))

if __name__ == "__main__":
    for _ in range(T):
        strInput = input()
        left = deque()
        right = deque()
        for i in range(len(strInput)):
            if strInput[i] == '<':
                if len(left) < 1:
                    continue
                cache = left.pop()
                right.appendleft(cache)
            elif strInput[i] == '>':
                if len(right) < 1:
                    continue
                cache = right.popleft()
                left.append(cache)
            elif strInput[i] == '-':
                if len(left) < 1:
                    continue
                left.pop()
            else:
                left.append(strInput[i])
        print(''.join(left + right))