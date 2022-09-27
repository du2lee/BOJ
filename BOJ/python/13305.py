N = int(input())

gas = [0] + list(map(int,input().split()))
nodes = list(map(int, input().split()))

dp = [0] * N
min = 10001

for i in range(1, N):
    if nodes[i - 1] < min:
        min = nodes[i - 1]

    dp[i] += dp[i - 1] + min * gas[i]

print(dp[-1])















# N = int(input())
# lines = list(map(int, input().split()))
# gas = list(map(int, input().split()))

# answer = 0
# minNum = 1000000000

# for i in range(N - 1):
#     if gas[i] < minNum:
#         minNum = gas[i]
#     answer += minNum * lines[i]

# print(answer)