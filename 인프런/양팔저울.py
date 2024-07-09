K = int(input())
kgs = list(map(int, input().split()))
sumKgs = sum(kgs)

check = [False for _ in range(sumKgs + 1)]

def dfs(n, lHap, rHap):
    if n >= K:
        cache = abs(lHap - rHap)
        check[cache] = True
        return
    
    # 아무것도 안하기
    dfs(n + 1, lHap, rHap)
    # 왼쪽에 두기
    dfs(n + 1, lHap + kgs[n], rHap)
    # 오른쪽에 두기
    dfs(n + 1, lHap, rHap + kgs[n])

dfs(0, 0, 0)

answer = 0

for flag in check:
    if not flag:
        answer += 1

print(answer)
    
    