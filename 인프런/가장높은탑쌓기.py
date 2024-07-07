N = int(input())

info = []

for _ in range(N):
    info.append(list(map(int, input().split())))

info.sort(reverse = True)

dp = [info[0][1]]

answer = 0

for idx in range(1, N):
    cache = 0

    for idx2 in range(idx - 1, -1, -1):
        weight = info[idx2][2]
        if(weight > info[idx][2]):
            cache = max(cache, dp[idx2] + info[idx][1])

    if cache == 0:
        dp.append(info[idx][1])
    else:
        dp.append(cache)

    answer = max(answer , cache)

print(answer)