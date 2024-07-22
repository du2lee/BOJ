N, M = list(map(int, input().split()))

check = [False for _ in range(N + 1)]
answer = 0

def dfs(n, arr, check):
    global answer

    if n > M:
        for v in arr:
            print(v, end = " ")
        print()
        answer += 1
        return
    
    for i in range(1, N + 1):
        if check[i]:
            continue
        check[i] = True
        dfs(n + 1, arr + [i], check)
        check[i] = False

dfs(1, [], check)
print(answer)