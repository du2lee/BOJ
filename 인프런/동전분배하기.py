from math import inf

N = int(input())

coins = []

for _ in range(N):
    coins.append(int(input()))

A = 0
B = 0
C = 0
answer = inf

def dfs(idx):
    global A, B, C, answer

    if idx == N:
        if A != B and B != C and A != C:
            arr = [A, B, C]
            arr.sort()
            answer = min(answer, arr[2] - arr[0])
        return

    A += coins[idx]
    dfs(idx + 1)
    A -= coins[idx]
    
    B += coins[idx]
    dfs(idx + 1)
    B -= coins[idx]

    C += coins[idx]
    dfs(idx + 1)
    C -= coins[idx]

dfs(0)

print(answer)