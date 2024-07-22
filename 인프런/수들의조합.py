N, K = list(map(int, input().split()))
array = list(map(int, input().split()))
M = int(input())

answer = 0

def dfs(n, arr, idx):
    global answer
    if n > K:
        if sum(arr) % M == 0:
            answer += 1
        return
    
    for i in range(idx, N):
        dfs(n + 1, arr + [array[i]], i + 1)

dfs(1, [], 0)
print(answer)
