N = int(input())

classes = [(0, 0)]

for _ in range(N):
    T, P = list(map(int, input().split()))
    classes.append((T, P))

answer = -1

def dfs(n, cost, pre):
    global answer
    if n > N:
        if classes[pre][0] + pre > n:
            cost -= classes[pre][1]
        answer = max(cost, answer)
        return
    
    t, p = classes[n]

    # 포함 안 되었을 때
    dfs(n + 1, cost, pre)

    # 포함 되었을 때
    if classes[pre][0] + pre <= n:
        dfs(n + 1, cost + p, n)

dfs(1, 0, 0)
print(answer)
    