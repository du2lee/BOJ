N = int(input())
lines = list(map(int, input().split()))
gas = list(map(int, input().split()))

answer = 0
minNum = 1000000000

for i in range(N - 1):
    if gas[i] < minNum:
        minNum = gas[i]
    answer += minNum * lines[i]

print(answer)