N = int(input())
arr = list(map(int, input().split()))

answer = "NO"

def dfs(n, A, B):
    global answer
    
    if n >= N:
        if sum(A) == sum(B):
            answer = "YES"
        return
    
    dfs(n + 1, A + [arr[n]], B)
    dfs(n + 1, A, B + [arr[n]])

dfs(0, [], [])

print(answer)