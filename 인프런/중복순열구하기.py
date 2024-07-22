N, M = list(map(int, input().split()))

answer = 0

def dfs(n, arr):
    global answer

    if n > M:
        answer += 1
        for v in arr:
            print(v, end = " ")
        print()
        return
    
    for idx in range(1, N + 1):
        dfs(n + 1, arr + [idx])

dfs(1, [])
print(answer)