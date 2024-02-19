N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

mid = N // 2
start = mid
end = mid + 1
answer = 0

for idx in range(mid):
    answer += sum(field[idx][start - idx : end + idx])
    answer += sum(field[N - 1 - idx][start - idx : end + idx])
answer += sum(field[mid])
print(answer)