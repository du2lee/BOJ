from collections import deque
result = deque()

def func(N):
    if len(result) == 6:
        print(*result)
        return

    for i in range(N, len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
            func(i + 1)
            result.pop()


while True:
    arr = deque(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.popleft()
    func(0)
    print('')












# import sys
# from collections import deque

# cache_array = deque()

# def func(n):

#     if len(cache_array) == 6:
#         print(*cache_array)
#         return

#     for i in range(n, len(array)):
#         if array[i] not in cache_array:
#             cache_array.append(array[i])
#             func(i + 1)
#             cache_array.pop()

# while True:
#     array = deque(map(int, sys.stdin.readline().split()))

#     if array[0] == 0 and len(array) == 1:
#         break
#     N = array.popleft()
#     func(0)
#     print('')