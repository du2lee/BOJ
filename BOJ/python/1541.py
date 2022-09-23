N = input().split('-')

result = [0] * len(N)

for idx in range(len(N)):
    if N[idx] == '':
        result[idx] = 0
        continue
    cache = ''
    for i in N[idx]:
        if i == '+':
            result[idx] += int(cache)
            cache = ''
        else:
            cache += i
    result[idx] += int(cache)
answer = result[0]

for i in result[1:]:
    answer -= i

print(answer)














# result = [ [0, 0] for _ in range(len(N))]
# arr = [0] * len(N)

# for idx in range(len(N)):
#     if N[idx] == '':
#         result[idx][1] = 0
#         continue
#     cache = ''
#     for i in N[idx]:
#         if i == '+':
#             result[idx][0] = 1
#             result[idx][1] += int(cache)
#             cache = ''
#         else:
#             cache += i
#     result[idx][1] += int(cache)
# arr[0] = result[0][1]

# for idx in range(1, len(N)):
#     cache = '-'
#     for i in N[idx]:
#         if i == '+':
#             arr[idx] += int(cache)
#             cache = ''
#         else:
#             cache += i
#     arr[idx] += int(cache)

# if len(N) > 1:
#     minus = max(result[1:])
#     idx = result[1:].index(minus)
#     print(sum(arr) - arr[idx + 1] - minus[1])
# else:
#     print(result[0][1])