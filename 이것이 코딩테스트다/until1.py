N, K = list(map(int, input().split()))

count = 0

while N > 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        a  = N % K
        N -= a
        count += a

if N != 1:
    count -= 1 - N

print(count)


# # N이 10만 초과 시 힘들어 질 수도
# count = 0

# while N > 1:
#     if N % K == 0:
#         N //= K
#     else:
#         N -= 1
#     count += 1

# print(count)