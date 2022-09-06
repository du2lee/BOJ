import sys

sys.setrecursionlimit(111111)


N = int(input())

graph = [[] for _ in range(N + 1)]
check = [-1 for _ in range(N + 1)]
result = check.copy()

for i in range(N - 1):
    arr = list(map(int, input().split()))
    graph[arr[0]].append([arr[1], arr[2]])
    graph[arr[1]].append([arr[0], arr[2]])

def dfs(v, length, node):
    result[v] = length

    for n, l in graph[v]:
        if result[n] == -1:
            if result[node] < l + length:
                node = n
            node = dfs(n, l + length, node)
    return node

node = dfs(1, 0, 1)
result = check.copy()
node = dfs(node, 0, 0)

if result[node] == -1:
    print(0)
else:
    print(result[node])