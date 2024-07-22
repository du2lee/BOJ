N = int(input())

def dfs(n, arr):
    if n > N:
        if len(arr) > 0:
            for v in arr:
                print(v, end = " ")
            print()
        return
    dfs(n + 1, arr + [n])
    dfs(n + 1, arr)

dfs(1, [])