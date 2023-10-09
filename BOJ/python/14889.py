A = []
B = []
answer = 10e9

def dfs(num, a, b):
    global answer
    if len(A) > N // 2 or len(B) > N // 2:
        return
    if num >= N + 1:
        value = abs(a - b)

        if answer > value:
            answer = value
        return
    
    # A팀 입장
    for player in A:
        a += graph[num - 1][player - 1]
        a += graph[player - 1][num - 1]
    A.append(num)
    dfs(num + 1, a, b)
    A.pop()
    for player in A:
        a -= graph[num - 1][player - 1]
        a -= graph[player - 1][num - 1]

    # B팀 입장
    for player in B:
        b += graph[num - 1][player - 1]
        b += graph[player - 1][num - 1]
    B.append(num)
    dfs(num + 1, a, b)
    B.pop()
    for player in B:
        b -= graph[num - 1][player - 1]
        b -= graph[player - 1][num - 1]


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dfs(1, 0, 0)
print(answer)