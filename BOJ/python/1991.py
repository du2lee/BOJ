N = int(input())

graph = dict()

for _ in range(N):
    arr = input().split()
    graph[arr[0]] = [arr[1], arr[2]]

def dfsFront(v):
    print(v, end = '')
    for i in graph[v]:
        if i == '.':
            continue
        dfsFront(i)

def dfsMid(v):

    i = graph[v][0]
    if i == '.':
        pass
    else:
        dfsMid(i)
    print(v, end = '')
    i = graph[v][1]
    if i == '.':
        pass
    else:
        dfsMid(i)

def dfsBack(v):
    for i in graph[v]:
        if i == '.':
            continue
        dfsBack(i)
    print(v, end = '')


dfsFront('A')
print()
dfsMid('A')
print()
dfsBack('A')
print()