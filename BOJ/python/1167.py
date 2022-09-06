V = int(input())
graph = [[] for _ in range(V + 1)]
example = [-1 for _ in range(V + 1)]
visited = example.copy()

for i in range(V):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr) - 1):
        if j % 2 == 1:
            graph[arr[0]].append([arr[j]])
        else:
            graph[arr[0]][j // 2 - 1].append(arr[j])

def dfs(v, length, node):
    visited[v] = length
    
    for n, l in graph[v]:
        if visited[n] == -1:
            if visited[node] < l + length:
                node = n
            node = dfs(n, l + length, node)
    return node

node = dfs(2, 0, 0)
visited = example
node = dfs(node, 0, 0)
print(visited[node])