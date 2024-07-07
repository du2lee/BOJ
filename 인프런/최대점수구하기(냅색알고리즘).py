# ====== S : 앞에서 계산 =======

# from copy import deepcopy

# N, M = list(map(int, input().split()))

# questions = []

# for _ in range(N):
#     questions.append(list(map(int, input().split())))

# dps = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

# for i in range(1, N + 1):
#     score, time = questions[i - 1]

#     dps[i] = deepcopy(dps[i - 1])
    
#     for idx in range(time, M + 1):
#         dps[i][idx] = max(dps[i - 1][idx - time] + score, dps[i][idx])

# print(dps[-1][-1])

# ====== E : 앞에서 계산 =======

# ====== S : 뒤에서 계산 =======

N, M = list(map(int, input().split()))

questions = []

for _ in range(N):
    questions.append(list(map(int, input().split())))

dp = [0 for _ in range(M + 1)]

for score, time in questions:
    
    for idx in range(M, time - 1, -1):
        dp[idx] = max(dp[idx], dp[idx - time] + score)
        
print(dp[-1])

# ====== E : 뒤에서 계산 =======