C, N = list(map(int, input().split()))

dogs = []

for _ in range(N):
    dogs.append(int(input()))

answer = 0
total = sum(dogs)

def dfs(idx, kg, tsum):
    global answer
    if kg + (total - tsum) < answer:
        return

    if kg > C:
        return

    if idx >= N:
        if kg <= C:
            answer = max(answer, kg)
        return
    dfs(idx + 1, kg + dogs[idx], tsum + dogs[idx])
    dfs(idx + 1, kg, tsum + dogs[idx])

dfs(0, 0, 0)
print(answer)