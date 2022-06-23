N = int(input())

array = list(map(int, input().split()))
reArray = array.copy()
reArray.reverse()
dp = [0] * N
reDp = [0] * N
finalDp = [0] * N
dp[0] = 1
reDp[0] = 1

for idx in range(N):
    count = 0
    flag = False

    for i in range(len(array[:idx])):
        if array[i] < array[idx] and count < dp[i]:
            count = dp[i]
            flag = True

    if flag:
        dp[idx] += count + 1
    else:
        dp[idx] = 1

for idx in range(N):
    reCount = 0
    reFlag = False

    for i in range(len(reArray[:idx])):
        if reArray[i] < reArray[idx] and reCount < reDp[i]:
            reCount = reDp[i]
            reFlag = True

    if reFlag:
        reDp[idx] += reCount + 1
    else:
        reDp[idx] = 1

reDp.reverse()
    
for idx in range(len(reDp)):
    finalDp[idx] = dp[idx] + reDp[idx] - 1

print(max(finalDp))

