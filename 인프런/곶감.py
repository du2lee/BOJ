N = int(input())
graph =[list(map(int, input().split())) for _ in range(N)]
for _ in range(int(input())):
    n, d, r = list(map(int, input().split()))
    n -= 1
    r = r % N
    if r == 0:  # 회전 X
        continue
    if d == 1: # 오른쪽
        left = graph[n][:N - r]
        right = graph[n][N - r:]
        graph[n] = right + left
    else: # 왼쪽
        left = graph[n][:r]
        right = graph[n][r :]
        graph[n] = right + left

s = 0
e = N
answer = 0
for idx in range(N // 2):
    answer += sum(graph[idx][s + idx : e - idx])
    answer += sum(graph[N - 1 - idx][s + idx : e - idx])
print(answer + graph[N // 2][N // 2])
