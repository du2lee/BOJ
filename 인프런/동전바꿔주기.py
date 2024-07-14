T = int(input())
k = int(input())

wallet = []

for _ in range(k):
    p, n = list(map(int, input().split()))
    wallet.append((p, n))

answer = 0

def dfs(amount, idx):
    global answer

    if amount > T:
        return
    
    if amount == T:
        answer += 1
        return

    if idx >= k:
        return

    for i in range(wallet[idx][1] + 1):
        dfs(amount + wallet[idx][0] * i, idx + 1)

dfs(0, 0)
print(answer)


    