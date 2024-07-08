from math import inf

N = int(int(input()))

dp = [[inf for _ in range(N + 1)] for __ in range(N + 1)]

for idx in range(1, N + 1):
    dp[idx][idx] = 0

while True:
    p1, p2 = list(map(int, input().split()))

    if(p1 == -1 and p2 == -1):
        break

    dp[p1][p2] = 1
    dp[p2][p1] = 1

for idx in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = min(dp[i][j], dp[i][idx] + dp[idx][j])

answer = [inf]

for i in range(1, N + 1):
    cache = -1
    for j in range(1, N + 1):
        score = dp[i][j]
        cache = max(cache, score)
    answer.append(cache)

ans = []
check = inf

for i in range(1, N + 1):
    cache = answer[i]

    if cache < check:
        ans = []
        ans.append(i)
        check = cache
    elif cache == check:
        ans.append(i)

print(check, end= " ")
print(len(ans))
for num in ans:
    print(num, end = " ")

    
