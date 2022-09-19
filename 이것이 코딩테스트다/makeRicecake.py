N, M = list(map(int, input().split()))

array = list(map(int, input().split()))
array.sort(reverse=True)

start = 0
end = array[0]
result = -1

while start <= end:
    mid = (start + end) // 2
    cache = 0
    for i in array:
        if i <= mid:
            break
        cache += i - mid
    
    if cache < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

    







# import sys

# N, M = list(map(int, sys.stdin.readline().rstrip().split()))
# ricecakes = list(map(int, sys.stdin.readline().rstrip().split()))

# ricecakes.sort(reverse=True)

# start = 0
# end = ricecakes[0]
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     total = 0
#     for i in ricecakes:
#         if i > mid:
#             total += i - mid
    
#     if total < M:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1

# print(result)
