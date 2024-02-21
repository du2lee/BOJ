N = int(input())

timeTable = []

for _ in range(N):
    s, e = list(map(int, input().split()))
    timeTable.append((e, s))

timeTable.sort()

answer = 0
end = 0

for e, s in timeTable:
    if end <= s:
        end = e
        answer += 1

print(answer)
