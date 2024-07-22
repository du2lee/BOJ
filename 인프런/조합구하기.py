N, M = list(map(int, input().split()))

answer = 0

def dfs(n, arr, s):
    global answer
    if n > M:
        for v in arr:
            print(v, end = " ")
        print()
        answer += 1
        return
    
    for i in range(s, N + 1):
        dfs(n + 1, arr + [i], i + 1)

dfs(1, [], 1)
print(answer)